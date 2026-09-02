import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, g, flash, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

import data
import translations
import tts

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "wardha-advisory-hackathon-demo-key-change-in-production")

DATABASE = "wardha_advisory.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DATABASE)
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('farmer', 'officer')),
            full_name TEXT NOT NULL,
            phone TEXT,
            village TEXT,
            preferred_lang TEXT DEFAULT 'en'
        );

        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            farmer_id INTEGER NOT NULL,
            crop TEXT NOT NULL,
            month TEXT NOT NULL,
            reported_price INTEGER NOT NULL,
            days_to_loan_due INTEGER NOT NULL,
            monsoon_delay_weeks INTEGER NOT NULL,
            problem_text TEXT,
            risk_score REAL NOT NULL,
            risk_status TEXT NOT NULL,
            reasons TEXT,
            verified_by_officer INTEGER DEFAULT 0,
            notified_ngo INTEGER DEFAULT 0,
            created_at TEXT NOT NULL,
            FOREIGN KEY (farmer_id) REFERENCES users (id)
        );
        """
    )
    existing = db.execute("SELECT id FROM users WHERE role = 'officer'").fetchone()
    if existing is None:
        db.execute(
            "INSERT INTO users (username, password_hash, role, full_name, phone, village, preferred_lang) "
            "VALUES (?, ?, 'officer', ?, ?, ?, 'en')",
            ("officer1", generate_password_hash("wardha123"), "Agro Officer (Wardha)", "9999999999", "Wardha"),
        )
        db.commit()
    db.close()


def current_user():
    user_id = session.get("user_id")
    if user_id is None:
        return None
    return get_db().execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()


def get_lang():
    if "lang" in session:
        return session["lang"]
    user = current_user()
    if user is not None:
        return user["preferred_lang"]
    return "en"


@app.context_processor
def inject_translation_helpers():
    lang = get_lang()
    return dict(
        t=lambda key: translations.t(key, lang),
        t_crop=lambda crop: translations.t_crop(crop, lang),
        t_month=lambda month: translations.t_month(month, lang),
        t_status=lambda status: translations.t_status(status, lang),
        num=lambda value: translations.num(value, lang),
        t_variety=lambda v: translations.t_variety(v, lang),
        t_submandi=lambda c: translations.t_submandi_commodities(c, lang),
        t_month_abbr=lambda m: translations.t_month_abbr(m, lang),
        t_stt=lambda l: translations.t_stt(l, lang),
        current_lang=lang,
        language_names=translations.LANGUAGE_NAMES,
        user=current_user(),
    )


@app.route("/set-language/<lang>")
def set_language(lang):
    if lang in ("en", "hi", "mr"):
        session["lang"] = lang
    return redirect(request.referrer or url_for("home"))


def require_role(role):
    user = current_user()
    if user is None:
        flash("Please log in first.")
        return redirect(url_for("login"))
    if user["role"] != role:
        flash("You don't have access to that page.")
        return redirect(url_for("login"))
    return None


@app.route("/")
def home():
    user = current_user()
    if user is not None:
        if user["role"] == "farmer":
            return redirect(url_for("farmer_dashboard"))
        return redirect(url_for("officer_dashboard"))

    mandi_prices = data.MANDI_PRICES
    rainfall_data = data.RAINFALL_BY_MONTH
    crop_varieties = {
        "Soybean": "Yellow (FAQ)",
        "Tur": "Red Gram (Whole)",
        "Cotton": "Unginned",
        "Gram": "Gram Whole / Kanta",
        "Wheat": "Deshi / Other",
        "Moong": "Whole",
        "Jowar": "Yellow / Hybrid",
        "Sesamum": "White / Other",
    }
    sub_mandis = [
        {"name": "Hinganghat APMC", "commodities": "Soybean, Cotton, Tur", "price_range": "₹4,900 – ₹6,620 / Qtl"},
        {"name": "Wardha Main APMC", "commodities": "Wheat, Tur, Bengal Gram, Sesame", "price_range": "₹6,250 – ₹8,045 / Qtl"},
        {"name": "Sindi Branch Seloo APMC", "commodities": "Soybean, Tur", "price_range": "₹5,800 – ₹6,200 / Qtl"},
        {"name": "Arvi & Ashti APMC", "commodities": "Soybean, Gram", "price_range": "₹5,500 – ₹6,500 / Qtl"},
    ]
    return render_template(
        "home.html",
        mandi_prices=mandi_prices,
        rainfall_data=rainfall_data,
        crop_varieties=crop_varieties,
        sub_mandis=sub_mandis,
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    role = request.form.get("role", "farmer") if request.method == "POST" else request.args.get("role", "farmer")
    if role not in ("farmer", "officer"):
        role = "farmer"

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        full_name = request.form["full_name"].strip()
        phone = request.form["phone"].strip()
        village = request.form["village"].strip()
        preferred_lang = request.form["preferred_lang"]

        db = get_db()
        existing = db.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
        if existing:
            flash("That username is already taken.")
            return render_template("login.html", role=role)

        db.execute(
            "INSERT INTO users (username, password_hash, role, full_name, phone, village, preferred_lang) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (username, generate_password_hash(password), role, full_name, phone, village, preferred_lang),
        )
        db.commit()
        flash("Account created. Please log in.")
        return redirect(url_for("login", role=role))

    return render_template("login.html", role=role)


@app.route("/login", methods=["GET", "POST"])
def login():
    role = request.args.get("role", "farmer")
    if role not in ("farmer", "officer"):
        role = "farmer"

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

        if user is None or not check_password_hash(user["password_hash"], password):
            flash("Incorrect username or password.")
            return render_template("login.html", role=role)

        session["user_id"] = user["id"]
        session["lang"] = user["preferred_lang"]
        flash(f"Welcome back, {user['full_name']}.")

        if user["role"] == "farmer":
            return redirect(url_for("farmer_dashboard"))
        return redirect(url_for("officer_dashboard"))

    return render_template("login.html", role=role)


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out.")
    return redirect(url_for("home"))


@app.route("/api/check-user")
def check_user():
    username = request.args.get("username", "").strip()
    if not username:
        return {"exists": False}
    db = get_db()
    user = db.execute("SELECT role FROM users WHERE username = ?", (username,)).fetchone()
    if user:
        return {"exists": True, "role": user["role"]}
    return {"exists": False}


@app.route("/farmer/dashboard")
def farmer_dashboard():
    redirect_response = require_role("farmer")
    if redirect_response:
        return redirect_response

    user = current_user()
    db = get_db()
    reports = db.execute(
        "SELECT * FROM reports WHERE farmer_id = ? ORDER BY created_at DESC", (user["id"],)
    ).fetchall()

    recommendation = session.pop("last_recommendation", None)

    return render_template(
        "farmer_dashboard.html",
        user=user,
        reports=reports,
        crops=list(data.MANDI_PRICES.keys()),
        months=list(data.RAINFALL_BY_MONTH.keys()),
        recommendation=recommendation,
    )


@app.route("/farmer/submit", methods=["POST"])
def submit_report():
    redirect_response = require_role("farmer")
    if redirect_response:
        return redirect_response

    user = current_user()

    crop = request.form["crop"]
    month = request.form["month"]
    reported_price = int(request.form["reported_price"])
    days_to_loan_due = int(request.form["days_to_loan_due"])
    monsoon_delay_weeks = int(request.form["monsoon_delay_weeks"])
    problem_text = request.form.get("problem_text", "").strip()

    risk = data.compute_risk_score(month, crop, reported_price, days_to_loan_due)

    db = get_db()
    db.execute(
        """INSERT INTO reports
           (farmer_id, crop, month, reported_price, days_to_loan_due,
            monsoon_delay_weeks, problem_text, risk_score, risk_status,
            reasons, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            user["id"], crop, month, reported_price, days_to_loan_due,
            monsoon_delay_weeks, problem_text, risk["score"], risk["status"],
            " | ".join(risk["reasons"]), datetime.now().isoformat(timespec="seconds"),
        ),
    )
    db.commit()

    if risk["status"] == "flagged":
        flash("Your report was submitted and flagged for officer review.")
    else:
        flash("Your report was submitted.")

    recommendation = data.get_crop_recommendation(month, crop, problem_text, get_lang())

    session["last_recommendation"] = {
        "season": recommendation["season"],
        "recommendation": recommendation["recommendation"],
        "profit_tip": recommendation["profit_tip"],
    }

    return redirect(url_for("farmer_dashboard"))


@app.route("/farmer/report/<int:report_id>")
def farmer_view_report(report_id):
    redirect_response = require_role("farmer")
    if redirect_response:
        return redirect_response

    user = current_user()
    db = get_db()
    report = db.execute(
        "SELECT * FROM reports WHERE id = ? AND farmer_id = ?", (report_id, user["id"])
    ).fetchone()
    if report is None:
        flash("Report not found.")
        return redirect(url_for("farmer_dashboard"))

    advisory = data.get_advisory(report["crop"], report["monsoon_delay_weeks"], get_lang())
    return render_template("report_detail.html", report=report, advisory=advisory, user=user, viewer_role="farmer")


@app.route("/report/<int:report_id>/audio/<lang>")
def report_audio(report_id, lang):
    user = current_user()
    if user is None:
        flash("Please log in first.")
        return redirect(url_for("login"))

    db = get_db()
    report = db.execute("SELECT * FROM reports WHERE id = ?", (report_id,)).fetchone()
    if report is None:
        flash("Report not found.")
        return redirect(url_for("home"))

    if user["role"] == "farmer" and report["farmer_id"] != user["id"]:
        flash("You don't have access to that report.")
        return redirect(url_for("farmer_dashboard"))

    if lang not in ("en", "hi", "mr"):
        flash("Unsupported language.")
        return redirect(url_for("home"))

    os.makedirs("static/audio", exist_ok=True)
    cache_path = f"static/audio/report_{report_id}_{lang}.wav"

    if not os.path.exists(cache_path):
        advisory = data.get_advisory(report["crop"], report["monsoon_delay_weeks"], lang)
        full_text = f"{advisory['delay_action']} {advisory['crop_tip']}"
        try:
            audio_bytes = tts.synthesize_speech(full_text, lang)
        except (RuntimeError, Exception) as e:
            flash(str(e))
            return redirect(url_for("home"))
        with open(cache_path, "wb") as f:
            f.write(audio_bytes)

    return send_file(cache_path, mimetype="audio/wav")


@app.route("/officer/dashboard")
def officer_dashboard():
    redirect_response = require_role("officer")
    if redirect_response:
        return redirect_response

    user = current_user()
    db = get_db()
    reports = db.execute(
        """SELECT reports.*, users.full_name AS farmer_name, users.phone AS farmer_phone,
                  users.village AS farmer_village
           FROM reports
           JOIN users ON reports.farmer_id = users.id
           ORDER BY reports.risk_score DESC, reports.created_at DESC"""
    ).fetchall()

    return render_template("officer_dashboard.html", user=user, reports=reports)


@app.route("/officer/report/<int:report_id>")
def officer_view_report(report_id):
    redirect_response = require_role("officer")
    if redirect_response:
        return redirect_response

    user = current_user()
    db = get_db()
    report = db.execute(
        """SELECT reports.*, users.full_name AS farmer_name, users.phone AS farmer_phone,
                  users.village AS farmer_village
           FROM reports
           JOIN users ON reports.farmer_id = users.id
           WHERE reports.id = ?""",
        (report_id,),
    ).fetchone()
    if report is None:
        flash("Report not found.")
        return redirect(url_for("officer_dashboard"))

    advisory = data.get_advisory(report["crop"], report["monsoon_delay_weeks"], get_lang())
    return render_template("report_detail.html", report=report, advisory=advisory, user=user, viewer_role="officer")


@app.route("/officer/report/<int:report_id>/verify", methods=["POST"])
def verify_report(report_id):
    redirect_response = require_role("officer")
    if redirect_response:
        return redirect_response

    db = get_db()
    db.execute("UPDATE reports SET verified_by_officer = 1 WHERE id = ?", (report_id,))
    db.commit()
    flash("Marked as verified.")
    return redirect(url_for("officer_view_report", report_id=report_id))


@app.route("/officer/report/<int:report_id>/mark-notified", methods=["POST"])
def mark_notified(report_id):
    redirect_response = require_role("officer")
    if redirect_response:
        return redirect_response

    db = get_db()
    db.execute("UPDATE reports SET notified_ngo = 1 WHERE id = ?", (report_id,))
    db.commit()
    flash("Marked as NGO notified.")
    return redirect(url_for("officer_view_report", report_id=report_id))


@app.route("/api/tts")
def api_tts():
    text = request.args.get("text", "").strip()
    lang = request.args.get("lang", "en")

    if not text:
        return {"error": "No text provided"}, 400
    if lang not in ("en", "hi", "mr"):
        return {"error": "Unsupported language"}, 400

    try:
        audio_bytes = tts.synthesize_speech(text, lang)
        return send_file(
            __import__("io").BytesIO(audio_bytes),
            mimetype="audio/wav",
            download_name="speech.wav",
        )
    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5001)
