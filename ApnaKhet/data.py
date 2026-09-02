RAINFALL_BY_MONTH = {
    "May":       {"normal_mm": 15.0,  "actual_mm": 110.3, "pct_of_normal": 735.3},
    "June":      {"normal_mm": 174.1, "actual_mm": 123.5, "pct_of_normal": 70.9},
    "July":      {"normal_mm": 273.6, "actual_mm": 341.9, "pct_of_normal": 125.0},
    "August":    {"normal_mm": 271.6, "actual_mm": 254.5, "pct_of_normal": 93.7},
    "September": {"normal_mm": 155.2, "actual_mm": 295.7, "pct_of_normal": 190.5},
    "October":   {"normal_mm": 52.9,  "actual_mm": 64.2,  "pct_of_normal": 121.4},
    "November":  {"normal_mm": 17.0,  "actual_mm": 5.7,   "pct_of_normal": 33.5},
    "December":  {"normal_mm": 15.1,  "actual_mm": 0.0,   "pct_of_normal": 0.0},
}

MANDI_PRICES = {
    "Soybean":     {"min": 4900,  "max": 7300,  "modal": 6265},
    "Tur":         {"min": 6025,  "max": 8045,  "modal": 7795},
    "Cotton":      {"min": 7110,  "max": 7600,  "modal": 7500},
    "Gram":        {"min": 5605,  "max": 6220,  "modal": 6175},
    "Wheat":       {"min": 2480,  "max": 2695,  "modal": 2650},
    "Moong":       {"min": 6500,  "max": 6500,  "modal": 6500},
    "Jowar":       {"min": 2000,  "max": 2480,  "modal": 2028},
    "Sesamum":     {"min": 11900, "max": 11900, "modal": 11900},
}

MONSOON_DELAY_ACTIONS = {
    0: {
        "en": "Monsoon on schedule. Continue normal crop and variety choice with standard package of practices.",
        "hi": "मानसून समय पर है। सामान्य फसल एवं किस्म तथा मानक कृषि पद्धतियाँ जारी रखें।",
        "mr": "मान्सून वेळेवर आहे. नेहमीचे पीक व वाण तसेच प्रमाणित कृषी पद्धती सुरू ठेवा.",
    },
    2: {
        "en": "Up to 2 weeks' delay (sow by 25 Jun-1 Jul). Continue normal crop/variety; standard package of practices.",
        "hi": "2 सप्ताह तक की देरी (25 जून-1 जुलाई तक बुवाई करें)। सामान्य फसल/किस्म जारी रखें; मानक कृषि पद्धतियाँ अपनाएं।",
        "mr": "2 आठवड्यांपर्यंत विलंब (25 जून-1 जुलैपर्यंत पेरणी करा). नेहमीचे पीक/वाण सुरू ठेवा; प्रमाणित कृषी पद्धती वापरा.",
    },
    4: {
        "en": "4 weeks' delay (sow by 9-15 Jul). Shift to short-duration varieties, increase seed rate by 20-25%, reduce fertilizer by 25% for cotton.",
        "hi": "4 सप्ताह की देरी (9-15 जुलाई तक बुवाई करें)। अल्पावधि किस्मों की ओर जाएं, बीज दर 20-25% बढ़ाएं, कपास के लिए उर्वरक 25% कम करें।",
        "mr": "4 आठवड्यांचा विलंब (9-15 जुलैपर्यंत पेरणी करा). अल्पकालीन वाणांकडे वळा, बियाणे दर 20-25% वाढवा, कापसासाठी खत 25% कमी करा.",
    },
    6: {
        "en": "6 weeks' delay (sow by 23-29 Jul). Switch to sole pigeon pea, sunflower, sesame, castor or pearl millet, with closer spacing.",
        "hi": "6 सप्ताह की देरी (23-29 जुलाई तक बुवाई करें)। केवल अरहर, सूरजमुखी, तिल, अरंडी या बाजरा लगाएं, पौधों के बीच दूरी कम रखें।",
        "mr": "6 आठवड्यांचा विलंब (23-29 जुलैपर्यंत पेरणी करा). फक्त तूर, सूर्यफूल, तीळ, एरंड किंवा बाजरी लावा, रोपांमधील अंतर कमी ठेवा.",
    },
    8: {
        "en": "8 weeks' delay (sow by 6-12 Aug). Only short-duration contingency crops (pigeon pea, sesame, pearl millet); in-situ moisture conservation is essential.",
        "hi": "8 सप्ताह की देरी (6-12 अगस्त तक बुवाई करें)। केवल अल्पावधि आकस्मिक फसलें (अरहर, तिल, बाजरा); स्थल पर नमी संरक्षण आवश्यक है।",
        "mr": "8 आठवड्यांचा विलंब (6-12 ऑगस्टपर्यंत पेरणी करा). फक्त अल्पकालीन आकस्मिक पिके (तूर, तीळ, बाजरी); जागेवरच ओलावा जतन करणे आवश्यक आहे.",
    },
}

CROP_TIPS = {
    "Soybean": {"en": "Watch for yellow mosaic virus in humid spells; ensure field drainage.",
                "hi": "नमी वाले मौसम में पीला मोज़ेक वायरस देखें; खेत की जल निकासी सुनिश्चित करें।",
                "mr": "दमट हवामानात पिवळा मोझॅक विषाणू तपासा; शेतातील पाणी निचरा सुनिश्चित करा."},
    "Cotton":  {"en": "Monitor for pink bollworm; avoid excess nitrogen which attracts pests.",
                "hi": "गुलाबी सुंडी की निगरानी करें; अधिक नाइट्रोजन से बचें जो कीट आकर्षित करती है।",
                "mr": "गुलाबी बोंडअळीवर लक्ष ठेवा; जास्त नत्रामुळे किडी आकर्षित होतात, ते टाळा."},
    "Tur":     {"en": "Tur is relatively drought-hardy; prioritize it if moisture is limited.",
                "hi": "अरहर अपेक्षाकृत सूखा-सहिष्णु है; नमी सीमित होने पर इसे प्राथमिकता दें।",
                "mr": "तूर तुलनेने दुष्काळ सहनशील आहे; ओलावा मर्यादित असल्यास तिला प्राधान्य द्या."},
    "Wheat":   {"en": "Ensure timely irrigation at crown root initiation stage for best yield.",
                "hi": "सर्वोत्तम उपज के लिए मुकुट जड़ अवस्था पर समय पर सिंचाई सुनिश्चित करें।",
                "mr": "उत्तम उत्पन्नासाठी मुकुट मूळ अवस्थेत वेळेवर सिंचन सुनिश्चित करा."},
    "Gram":    {"en": "Avoid waterlogging; gram is sensitive to excess soil moisture.",
                "hi": "जलभराव से बचें; चना अधिक मिट्टी की नमी के प्रति संवेदनशील है।",
                "mr": "पाणी साचणे टाळा; हरभरा जास्त मातीतील ओलाव्यास संवेदनशील आहे."},
    "Moong":   {"en": "Short-duration crop — good contingency option if sowing is delayed.",
                "hi": "अल्पावधि फसल — बुवाई में देरी होने पर अच्छा आकस्मिक विकल्प।",
                "mr": "अल्पकालीन पीक — पेरणीस विलंब झाल्यास चांगला पर्याय."},
    "Jowar":   {"en": "Relatively hardy under moisture stress; suitable as a delayed-sowing option.",
                "hi": "नमी के तनाव में अपेक्षाकृत सहनशील; देरी से बुवाई के लिए उपयुक्त।",
                "mr": "ओलाव्याच्या ताणाखाली तुलनेने सहनशील; उशिरा पेरणीसाठी योग्य."},
    "Sesamum": {"en": "Low water requirement; a reasonable short-duration fallback crop.",
                "hi": "कम पानी की आवश्यकता; अल्पावधि विकल्प के रूप में उपयुक्त।",
                "mr": "कमी पाण्याची गरज; अल्पकालीन पर्यायी पीक म्हणून योग्य."},
}


def compute_risk_score(month, crop, reported_price, days_to_loan_due):
    month_data = RAINFALL_BY_MONTH[month]
    rainfall_deficit = max(0.0, (month_data["normal_mm"] - month_data["actual_mm"]) / month_data["normal_mm"])

    modal_price = MANDI_PRICES[crop]["modal"]
    price_drop = max(0.0, (modal_price - reported_price) / modal_price)

    if days_to_loan_due <= 15:
        loan_proximity = 1 - (days_to_loan_due / 15)
    else:
        loan_proximity = 0.0

    score = 0.4 * rainfall_deficit + 0.4 * price_drop + 0.2 * loan_proximity
    score = min(1.0, score)

    reasons = []
    if rainfall_deficit > 0.15:
        reasons.append(f"Rainfall in {month} was {month_data['pct_of_normal']:.0f}% of normal")
    if price_drop > 0.08:
        reasons.append(f"Reported price is below the modal mandi price of ₹{modal_price}/quintal for {crop}")
    if loan_proximity > 0:
        reasons.append(f"Loan due in {days_to_loan_due} day(s)")

    if score >= 0.55:
        status = "flagged"
    elif score >= 0.30:
        status = "watch"
    else:
        status = "safe"

    return {
        "score": round(score, 3),
        "status": status,
        "reasons": reasons,
        "rainfall_deficit": round(rainfall_deficit, 3),
        "price_drop": round(price_drop, 3),
        "loan_proximity": round(loan_proximity, 3),
    }


def get_advisory(crop, monsoon_delay_weeks, lang):
    delay_action = MONSOON_DELAY_ACTIONS[monsoon_delay_weeks][lang]
    crop_tip = CROP_TIPS[crop][lang]
    return {"delay_action": delay_action, "crop_tip": crop_tip}


def get_crop_recommendation(month, crop, problem_text, lang):
    import translations

    kharif_months = ["June", "July", "August", "September"]
    rabi_months = ["October", "November", "December", "January", "February", "March"]
    summer_months = ["April", "May"]

    if month in kharif_months:
        season = "Kharif"
    elif month in rabi_months:
        season = "Rabi"
    else:
        season = "Summer"

    recommendation = translations.CROP_RECOMMENDATIONS[season][lang]

    modal = MANDI_PRICES[crop]["modal"]
    best_crop = max(MANDI_PRICES.items(), key=lambda x: x[1]["modal"])
    best_crop_name = best_crop[0]
    best_price = best_crop[1]["modal"]

    if lang == "hi":
        profit_tip = (f"वर्तमान में {translations.t_crop(crop, lang)} का मॉडल मूल्य ₹{modal}/क्विंटल है। "
                      f"सबसे अधिक लाभदायक फसल {translations.t_crop(best_crop_name, lang)} है जिसका मूल्य ₹{best_price}/क्विंटल है। "
                      f"अगले मौसम में {translations.t_crop(best_crop_name, lang)} पर विचार करें।")
    elif lang == "mr":
        profit_tip = (f"सध्या {translations.t_crop(crop, lang)} चा मॉडल भाव ₹{modal}/क्विंटल आहे. "
                      f"सर्वाधिक नफेकारक पीक {translations.t_crop(best_crop_name, lang)} आहे ज्याचा भाव ₹{best_price}/क्विंटल आहे. "
                      f"पुढच्या हंगामात {translations.t_crop(best_crop_name, lang)} याचा विचार करा.")
    else:
        profit_tip = (f"Currently, {crop} has a modal price of ₹{modal}/quintal. "
                      f"The most profitable crop is {best_crop_name} at ₹{best_price}/quintal. "
                      f"Consider {best_crop_name} for the next season.")

    return {
        "season": season,
        "recommendation": recommendation,
        "profit_tip": profit_tip,
    }
