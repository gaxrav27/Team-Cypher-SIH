# translations.py: all UI text in English, Hindi, Marathi

UI = {
    # --- nav / base layout ---
    "brand":            {"en": "Wardha Field Ledger", "hi": "वर्धा फील्ड लेजर", "mr": "वर्धा फील्ड लेजर"},
    "log_in":           {"en": "Log in", "hi": "लॉग इन", "mr": "लॉग इन"},
    "log_out":          {"en": "Log out", "hi": "लॉग आउट", "mr": "लॉग आउट"},
    "farmer_sign_up":   {"en": "Farmer sign up", "hi": "किसान पंजीकरण", "mr": "शेतकरी नोंदणी"},
    "login_as_farmer":  {"en": "Log in as Farmer", "hi": "किसान के रूप में लॉग इन", "mr": "शेतकरी म्हणून लॉग इन"},
    "login_as_officer": {"en": "Log in as Officer", "hi": "अधिकारी के रूप में लॉग इन", "mr": "अधिकारी म्हणून लॉग इन"},

    # --- hero ---
    "hero_badge":       {"en": "Smart Crop Advisory System", "hi": "स्मार्ट फसल सलाह प्रणाली", "mr": "स्मार्ट पीक सल्ला प्रणाली"},
    "home_title":       {"en": "Crop Advice & Farmer Distress Early Warning, Wardha",
                          "hi": "फसल सलाह और किसान संकट पूर्व चेतावनी, वर्धा",
                          "mr": "पीक सल्ला आणि शेतकरी संकट पूर्व इशारा, वर्धा"},
    "home_subtitle":    {"en": "Real rainfall, mandi prices, and drought data for Wardha, all from government sources.",
                          "hi": "वर्धा का असली वर्षा, मंडी भाव और सूखा डेटा, सब सरकारी स्रोतों से।",
                          "mr": "वर्ध्यासाठी खरा पाऊस, बाजार भाव आणि दुष्काळ डेटा, सरकारी स्रोतांकडून."},
    "hero_btn_farmer":  {"en": "I'm a Farmer", "hi": "मैं किसान हूँ", "mr": "मी शेतकरी आहे"},
    "hero_btn_officer": {"en": "I'm an Officer", "hi": "मैं अधिकारी हूँ", "mr": "मी अधिकारी आहे"},

    # --- weather section ---
    "weather_title":    {"en": "Live Weather, Wardha", "hi": "मौसम, वर्धा", "mr": "हवामान, वर्धा"},
    "weather_sub":      {"en": "Real-time conditions and forecasts", "hi": "वास्तविक समय में मौसम और पूर्वानुमान", "mr": "वास्तविक काळातील हवामान आणि अंदाज"},
    "weather_tab_today":    {"en": "Today", "hi": "आज", "mr": "आज"},
    "weather_tab_tomorrow": {"en": "Tomorrow", "hi": "कल", "mr": "उद्या"},
    "weather_tab_3day":     {"en": "3-Day", "hi": "3 दिन", "mr": "3 दिवस"},
    "weather_tab_7day":     {"en": "7-Day", "hi": "7 दिन", "mr": "7 दिवस"},
    "weather_loading":  {"en": "Fetching live weather data for Wardha...", "hi": "वर्धा का मौसम डेटा लोड हो रहा है...", "mr": "वर्धा चे हवामान डेटा लोड होत आहे..."},
    "weather_error":    {"en": "Unable to fetch live weather data. Check your connection.", "hi": "मौसम डेटा लोड नहीं हो सका। अपना कनेक्शन जांचें।", "mr": "हवामान डेटा लोड होऊ शकला नाही. तुमचे कनेक्शन तपासा."},
    "w_humidity":       {"en": "Humidity", "hi": "नमी", "mr": "ओलावा"},
    "w_wind":           {"en": "Wind", "hi": "हवा", "mr": "वारा"},
    "w_precipitation":  {"en": "Precipitation", "hi": "वर्षा", "mr": "पाऊस"},
    "w_feels_like":     {"en": "Feels Like", "hi": "अनुभव", "mr": "अनुभव"},
    "w_max_wind":       {"en": "Max Wind", "hi": "अधिकतम हवा", "mr": "जास्तीत जास्त वारा"},
    "w_total_rain":     {"en": "Total Rain", "hi": "कुल वर्षा", "mr": "एकूण पाऊस"},
    "w_temp_range":     {"en": "Temp Range", "hi": "तापमान", "mr": "तापमान"},
    "w_rain":           {"en": "Rain:", "hi": "वर्षा:", "mr": "पाऊस:"},

    # --- mandi section ---
    "mandi_title":      {"en": "Mandi Prices at Wardha APMCs", "hi": "मंडी भाव, वर्धा एपीएमसी", "mr": "बाजार भाव, वर्धा एपीएमसी"},
    "mandi_sub":        {"en": "2025–26 Marketing Season · Source: Agmarknet / Directorate of Marketing & Inspection",
                          "hi": "2025–26 विपणन मौसम · स्रोत: अगमर्केट / विपणन और निरीक्षण निदेशालय",
                          "mr": "2025–26 विपणन हंगाम · स्रोत: अगमर्केट / विपणन व निरीक्षण संचालनालय"},
    "mandi_commodity":  {"en": "Commodity", "hi": "वस्तु", "mr": "वस्तू"},
    "mandi_variety":    {"en": "Variety", "hi": "किस्म", "mr": "प्रकार"},
    "mandi_min":        {"en": "Min ₹/Qtl", "hi": "न्यून ₹/क्विं", "mr": "किमान ₹/क्विं"},
    "mandi_max":        {"en": "Max ₹/Qtl", "hi": "अधि ₹/क्विं", "mr": "कमाल ₹/क्विं"},
    "mandi_modal":      {"en": "Modal ₹/Qtl", "hi": "मॉडल ₹/क्विं", "mr": "मॉडल ₹/क्विं"},
    "mandi_avg":        {"en": "Avg ₹/Kg", "hi": "औसत ₹/किग्रा", "mr": "सरासरी ₹/किलो"},

    # --- sub-mandi section ---
    "submandi_title":   {"en": "Sub-Mandi Market Trends", "hi": "उप-मंडी बाजार रुझान", "mr": "उप-बाजार बाजार ट्रेंड"},
    "submandi_sub":     {"en": "Primary commodities traded across Wardha APMCs", "hi": "वर्धा एपीएमसी में व्यापारित प्रमुख वस्तुएं", "mr": "वर्धा एपीएमसीमध्ये व्यापारात असलेल्या प्रमुख वस्तू"},

    # --- rainfall section ---
    "rainfall_title":   {"en": "Rainfall Summary, Wardha 2025", "hi": "वर्षा सारांश, वर्धा 2025", "mr": "पाऊस सारांश, वर्धा 2025"},
    "rainfall_sub":     {"en": "Source: Districtwise Daily Rainfall Reports, Maharashtra", "hi": "स्रोत: जिला-वार दैनिक वर्षा रिपोर्ट, महाराष्ट्र", "mr": "स्रोत: जिल्हास्तरीय दैनिक पाऊस अहवाल, महाराष्ट्र"},
    "rainfall_actual":  {"en": "Actual Rainfall", "hi": "वास्तविक वर्षा", "mr": "प्रत्यक्ष पाऊस"},
    "rainfall_normal":  {"en": "District Normal", "hi": "जिला सामान्य", "mr": "जिल्हा सामान्य"},

    # --- CTA section ---
    "cta_title":        {"en": "Ready to get started?", "hi": "शुरू करने के लिए तैयार?", "mr": "सुरू करायला तयार?"},
    "cta_text":         {"en": "Submit crop reports, get personalized advisories, and connect with agricultural officers in your area.",
                          "hi": "फसल रिपोर्ट सबमिट करें, व्यक्तिगत सलाह प्राप्त करें, और अपने क्षेत्र के कृषि अधिकारियों से जुड़ें।",
                          "mr": "पीक अहवाल सबमिट करा, वैयक्तिक सल्ला मिळवा आणि तुमच्या भागातील शेती अधिकाऱ्यांशी जोडले जा."},

    # --- stats bar ---
    "stat_crops":       {"en": "Crops Tracked", "hi": "फसलें ट्रैक", "mr": "पिके ट्रॅक"},
    "stat_markets":     {"en": "APMC Markets", "hi": "एपीएमसी बाजार", "mr": "एपीएमसी बाजार"},
    "stat_rainfall":    {"en": "Annual Rainfall", "hi": "वार्षिक वर्षा", "mr": "वार्षिक पाऊस"},
    "stat_languages":   {"en": "Languages", "hi": "भाषाएं", "mr": "भाषा"},

    # --- login page ---
    "login_heading":    {"en": "Log in", "hi": "लॉग इन", "mr": "लॉग इन"},
    "farmer_portal":    {"en": "Farmer Portal", "hi": "किसान पोर्टल", "mr": "शेतकरी पोर्टल"},
    "officer_portal":   {"en": "Officer Portal", "hi": "अधिकारी पोर्टल", "mr": "अधिकारी पोर्टल"},
    "login_tab":        {"en": "Log In", "hi": "लॉग इन", "mr": "लॉग इन"},
    "signup_tab":       {"en": "Sign Up", "hi": "साइन अप", "mr": "साइन अप"},
    "login_subtitle":   {"en": "Welcome back! Enter your credentials to continue.", "hi": "स्वागत है! आगे बढ़ने के लिए अपनी जानकारी दर्ज करें।", "mr": "स्वागत आहे! पुढे जाण्यासाठी तुमची माहिती टाका."},
    "signup_subtitle":  {"en": "Create a new account to get started.", "hi": "शुरू करने के लिए एक नया खाता बनाएं।", "mr": "सुरू करण्यासाठी एक नवीन खाते तयार करा."},
    "username":         {"en": "Username", "hi": "उपयोगकर्ता नाम", "mr": "वापरकर्तानाव"},
    "password":         {"en": "Password", "hi": "पासवर्ड", "mr": "पासवर्ड"},
    "full_name":        {"en": "Full name", "hi": "पूरा नाम", "mr": "पूर्ण नाव"},
    "village":          {"en": "Village", "hi": "गाँव", "mr": "गाव"},
    "phone_number":     {"en": "Phone number", "hi": "फ़ोन नंबर", "mr": "फोन नंबर"},
    "preferred_lang":   {"en": "Preferred language", "hi": "पसंदीदा भाषा", "mr": "पसंतीची भाषा"},
    "create_account":   {"en": "Create account", "hi": "खाता बनाएं", "mr": "खाते तयार करा"},
    "login_hint":       {"en": "Demo officer account: officer1 / wardha123",
                          "hi": "डेमो अधिकारी खाता: officer1 / wardha123",
                          "mr": "डेमो अधिकारी खाते: officer1 / wardha123"},
    "placeholder_username":  {"en": "Enter your username", "hi": "अपना उपयोगकर्ता नाम दर्ज करें", "mr": "तुमचे वापरकर्तानाव टाका"},
    "placeholder_password":  {"en": "Enter your password", "hi": "अपना पासवर्ड दर्ज करें", "mr": "तुमचा पासवर्ड टाका"},
    "placeholder_fullname":  {"en": "Your full name", "hi": "अपना पूरा नाम", "mr": "तुमचे पूर्ण नाव"},
    "placeholder_phone":     {"en": "10-digit phone number", "hi": "10 अंकों का फ़ोन नंबर", "mr": "10 अंकांचा फोन नंबर"},
    "placeholder_village":   {"en": "Your village name", "hi": "अपने गाँव का नाम", "mr": "तुमच्या गावाचे नाव"},
    "placeholder_choose_user": {"en": "Choose a username", "hi": "एक उपयोगकर्ता नाम चुनें", "mr": "एक वापरकर्तानाव निवडा"},
    "placeholder_choose_pass": {"en": "Choose a password", "hi": "एक पासवर्ड चुनें", "mr": "एक पासवर्ड निवडा"},

    # --- farmer dashboard ---
    "welcome":              {"en": "Welcome", "hi": "स्वागत है", "mr": "स्वागत आहे"},
    "submit_new_report":    {"en": "Submit a new report", "hi": "नई रिपोर्ट सबमिट करें", "mr": "नवीन अहवाल सबमिट करा"},
    "crop":                 {"en": "Crop", "hi": "फसल", "mr": "पीक"},
    "month_concerned":      {"en": "Which month are you concerned about?",
                              "hi": "आप किस महीने को लेकर चिंतित हैं?",
                              "mr": "तुम्हाला कोणत्या महिन्याबद्दल चिंता आहे?"},
    "price_received":       {"en": "Price you actually received (₹ per quintal)",
                              "hi": "आपको वास्तव में मिली कीमत (₹ प्रति क्विंटल)",
                              "mr": "तुम्हाला प्रत्यक्ष मिळालेला भाव (₹ प्रति क्विंटल)"},
    "days_to_loan_due":     {"en": "Days until your loan payment is due",
                              "hi": "आपके ऋण भुगतान की देय तिथि तक कितने दिन बचे हैं",
                              "mr": "तुमच्या कर्ज परतफेडीची मुदत किती दिवसांत आहे"},
    "sowing_delay_q":       {"en": "How many weeks late was your sowing this season?",
                              "hi": "इस मौसम में आपकी बुवाई कितने सप्ताह देर से हुई?",
                              "mr": "या हंगामात तुमची पेरणी किती आठवडे उशिरा झाली?"},
    "delay_0":               {"en": "On time", "hi": "समय पर", "mr": "वेळेवर"},
    "delay_2":               {"en": "About 2 weeks late", "hi": "लगभग 2 सप्ताह देर से", "mr": "सुमारे 2 आठवडे उशिरा"},
    "delay_4":               {"en": "About 4 weeks late", "hi": "लगभग 4 सप्ताह देर से", "mr": "सुमारे 4 आठवडे उशिरा"},
    "delay_6":               {"en": "About 6 weeks late", "hi": "लगभग 6 सप्ताह देर से", "mr": "सुमारे 6 आठवडे उशिरा"},
    "delay_8":               {"en": "8+ weeks late", "hi": "8+ सप्ताह देर से", "mr": "8+ आठवडे उशिरा"},
    "describe_problem":     {"en": "Describe your problem (optional)",
                              "hi": "अपनी समस्या बताएं (वैकल्पिक)",
                              "mr": "तुमची समस्या सांगा (ऐच्छिक)"},
    "submit_report":        {"en": "Submit report", "hi": "रिपोर्ट सबमिट करें", "mr": "अहवाल सबमिट करा"},
    "your_past_reports":    {"en": "Your past reports", "hi": "आपकी पिछली रिपोर्टें", "mr": "तुमचे मागील अहवाल"},
    "no_reports_yet":       {"en": "No reports yet.", "hi": "अभी तक कोई रिपोर्ट नहीं।", "mr": "अजून कोणताही अहवाल नाही."},
    "date":                  {"en": "Date", "hi": "दिनांक", "mr": "तारीख"},
    "month":                 {"en": "Month", "hi": "महीना", "mr": "महिना"},
    "status":                {"en": "Status", "hi": "स्थिति", "mr": "स्थिती"},
    "view_advisory":        {"en": "View advisory", "hi": "सलाह देखें", "mr": "सल्ला पहा"},

    # --- officer dashboard ---
    "officer_heading":      {"en": "All Farmer Reports, Wardha", "hi": "सभी किसान रिपोर्टें, वर्धा", "mr": "सर्व शेतकरी अहवाल, वर्धा"},
    "officer_subtitle":     {"en": "Sorted by risk, highest first. Click a row to review, verify, or notify an NGO.",
                              "hi": "जोखिम के हिसाब से क्रमबद्ध, ज़्यादा जोखिम वाले पहले। पंक्ति पर क्लिक करें।",
                              "mr": "जोखीमानुसार क्रमवारी, सर्वाधिक आधी. ओळीवर क्लिक करा."},
    "farmer":                {"en": "Farmer", "hi": "किसान", "mr": "शेतकरी"},
    "risk":                  {"en": "Risk", "hi": "जोखिम", "mr": "जोखीम"},
    "verified":              {"en": "Verified", "hi": "सत्यापित", "mr": "पडताळणी झाली"},
    "ngo_notified":          {"en": "NGO notified", "hi": "एनजीओ को सूचित किया गया", "mr": "एनजीओला सूचित केले"},
    "review":                {"en": "Review", "hi": "समीक्षा करें", "mr": "पुनरावलोकन करा"},
    "no_reports_submitted": {"en": "No reports submitted yet.", "hi": "अभी तक कोई रिपोर्ट सबमिट नहीं हुई।", "mr": "अजून कोणताही अहवाल सबमिट झाला नाही."},
    "yes":                   {"en": "Yes", "hi": "हाँ", "mr": "होय"},
    "no":                    {"en": "No", "hi": "नहीं", "mr": "नाही"},

    # --- report detail page ---
    "report_heading":       {"en": "Report", "hi": "रिपोर्ट", "mr": "अहवाल"},
    "advisory":              {"en": "Advisory", "hi": "सलाह", "mr": "सल्ला"},
    "risk_signals":          {"en": "Risk signals", "hi": "जोखिम संकेत", "mr": "जोखीम संकेत"},
    "risk_score_label":     {"en": "Risk score", "hi": "जोखिम स्कोर", "mr": "जोखीम गुणांक"},
    "no_risk_signals":      {"en": "No elevated risk signals.", "hi": "कोई बढ़ा हुआ जोखिम संकेत नहीं।", "mr": "कोणतेही वाढलेले जोखीम संकेत नाहीत."},
    "farmer_own_desc":      {"en": "Farmer's own description", "hi": "किसान का अपना विवरण", "mr": "शेतकऱ्याचे स्वतःचे वर्णन"},
    "farmer_contact":       {"en": "Farmer contact", "hi": "किसान संपर्क", "mr": "शेतकरी संपर्क"},
    "mark_verified":        {"en": "Mark as verified (contacted farmer)",
                              "hi": "सत्यापित के रूप में चिह्नित करें (किसान से संपर्क किया)",
                              "mr": "पडताळणी केली म्हणून चिन्हांकित करा (शेतकऱ्याशी संपर्क केला)"},
    "notify_ngo_whatsapp":  {"en": "Notify NGO via WhatsApp", "hi": "व्हाट्सएप के माध्यम से एनजीओ को सूचित करें", "mr": "व्हॉट्सअॅपद्वारे एनजीओला सूचित करा"},
    "mark_notified_system": {"en": "Mark as notified in system", "hi": "सिस्टम में सूचित के रूप में चिह्नित करें", "mr": "प्रणालीमध्ये सूचित केले म्हणून चिन्हांकित करा"},
    "back":                  {"en": "Back", "hi": "वापस", "mr": "मागे"},
    "audio_not_supported":  {"en": "Your browser does not support audio playback.",
                              "hi": "आपका ब्राउज़र ऑडियो प्लेबैक का समर्थन नहीं करता।",
                              "mr": "तुमचा ब्राउझर ऑडिओ प्लेबॅकला समर्थन देत नाही."},

    # --- voice assistant prompts ---
    "va_greeting":      {"en": "Hello! I am your voice assistant. I will help you fill the report. Let us begin.",
                          "hi": "नमस्ते! मैं आपकी वॉइस असिस्टेंट हूँ। मैं आपकी रिपोर्ट भरने में मदद करूँगी। शुरू करते हैं।",
                          "mr": "नमस्कार! मी तुमची व्हॉइस असिस्टंट आहे. मी तुम्हाला अहवाल भरण्यास मदत करेन. सुरू करूया."},
    "va_ask_crop":      {"en": "What crop are you growing? Say the crop name.",
                          "hi": "आप कौन सी फसल उगा रहे हैं? फसल का नाम बोलें।",
                          "mr": "तुम्ही कोणते पीक लावत आहात? पिकाचे नाव सांगा."},
    "va_ask_month":     {"en": "Which month are you concerned about? Say the month name.",
                          "hi": "आप किस महीने को लेकर चिंतित हैं? महीने का नाम बोलें।",
                          "mr": "तुम्हाला कोणत्या महिन्याबद्दल चिंता आहे? महिन्याचे नाव सांगा."},
    "va_ask_price":     {"en": "What price did you receive per quintal? Say the number.",
                          "hi": "आपको प्रति क्विंटल कितना भाव मिला? संख्या बोलें।",
                          "mr": "तुम्हाला प्रति क्विंटल कितका भाव मिळाला? संख्या सांगा."},
    "va_ask_loan":      {"en": "How many days until your loan payment is due? Say the number.",
                          "hi": "आपके ऋण भुगतान की देय तिथि तक कितने दिन बचे हैं? संख्या बोलें।",
                          "mr": "तुमच्या कर्ज परतफेडीची मुदत किती दिवसांत आहे? संख्या सांगा."},
    "va_ask_delay":     {"en": "How many weeks late was your sowing? Say 0, 2, 4, 6 or 8.",
                          "hi": "आपकी बुवाई कितने सप्ताह देर से हुई? 0, 2, 4, 6 या 8 बोलें।",
                          "mr": "तुमची पेरणी किती आठवडे उशिरा झाली? 0, 2, 4, 6 किंवा 8 सांगा."},
    "va_ask_problem":   {"en": "Please describe your problem in detail.",
                          "hi": "कृपया अपनी समस्या विस्तार से बताएं।",
                          "mr": "कृपया तुमची समस्या तपशीलाने सांगा."},
    "va_confirm":       {"en": "Your report is ready. Review the fields and click Submit. Thank you!",
                          "hi": "आपकी रिपोर्ट तैयार है। फ़ील्ड्स देखें और सबमिट पर क्लिक करें। धन्यवाद!",
                          "mr": "तुमचा अहवाल तयार आहे. फील्ड्स तपासा आणि सबमिटवर क्लिक करा. धन्यवाद!"},
    "va_start":         {"en": "Start Voice Assistant", "hi": "वॉइस असिस्टेंट शुरू करें", "mr": "व्हॉइस असिस्टंट सुरू करा"},
    "va_stop":          {"en": "Stop Assistant", "hi": "असिस्टेंट बंद करें", "mr": "असिस्टंट थांबवा"},
    "va_listening":     {"en": "Listening...", "hi": "सुन रहे हैं...", "mr": "ऐकत आहे..."},
    "va_speaking":      {"en": "Speaking...", "hi": "बोल रहे हैं...", "mr": "बोलत आहे..."},
    "va_processing":    {"en": "Processing...", "hi": "प्रक्रिया हो रही है...", "mr": "प्रक्रिया होत आहे..."},
    "va_manual_mode":   {"en": "Or fill the form manually below", "hi": "या नीचे फॉर्म मैन्युअली भरें", "mr": "किंवा खालील फॉर्म मॅन्युअली भरा"},
    "va_crop_match":    {"en": "Detected crop:", "hi": "पहचानी गई फसल:", "mr": "ओळखलेले पीक:"},
    "va_month_match":   {"en": "Detected month:", "hi": "पहचाना गया महीना:", "mr": "ओळखलेला महिना:"},
    "va_no_match":      {"en": "Could not recognize. Please try again.", "hi": "पहचान नहीं हो सकी। कृपया फिर से कोशिश करें।", "mr": "ओळखता आले नाही. कृपया पुन्हा प्रयत्न करा."},
}

CROP_NAMES = {
    "Soybean": {"en": "Soybean", "hi": "सोयाबीन", "mr": "सोयाबीन"},
    "Tur":     {"en": "Tur (Pigeon Pea)", "hi": "अरहर (तूर)", "mr": "तूर"},
    "Cotton":  {"en": "Cotton", "hi": "कपास", "mr": "कापूस"},
    "Gram":    {"en": "Gram (Chickpea)", "hi": "चना", "mr": "हरभरा"},
    "Wheat":   {"en": "Wheat", "hi": "गेहूं", "mr": "गहू"},
    "Moong":   {"en": "Moong (Green Gram)", "hi": "मूंग", "mr": "मूग"},
    "Jowar":   {"en": "Jowar (Sorghum)", "hi": "ज्वार", "mr": "ज्वारी"},
    "Sesamum": {"en": "Sesamum (Til)", "hi": "तिल", "mr": "तीळ"},
}

MONTH_NAMES = {
    "May":       {"en": "May", "hi": "मई", "mr": "मे"},
    "June":      {"en": "June", "hi": "जून", "mr": "जून"},
    "July":      {"en": "July", "hi": "जुलाई", "mr": "जुलै"},
    "August":    {"en": "August", "hi": "अगस्त", "mr": "ऑगस्ट"},
    "September": {"en": "September", "hi": "सितंबर", "mr": "सप्टेंबर"},
    "October":   {"en": "October", "hi": "अक्टूबर", "mr": "ऑक्टोबर"},
    "November":  {"en": "November", "hi": "नवंबर", "mr": "नोव्हेंबर"},
    "December":  {"en": "December", "hi": "दिसंबर", "mr": "डिसेंबर"},
}

STATUS_LABELS = {
    "safe":    {"en": "Stable", "hi": "स्थिर", "mr": "स्थिर"},
    "watch":   {"en": "Watch", "hi": "निगरानी", "mr": "निरीक्षण"},
    "flagged": {"en": "Flagged", "hi": "चिन्हित", "mr": "चिन्हांकित"},
}

# Crop variety translations
VARIETY_NAMES = {
    "Yellow (FAQ)":       {"en": "Yellow (FAQ)", "hi": "पीला (FAQ)", "mr": "पिवळा (FAQ)"},
    "Red Gram (Whole)":   {"en": "Red Gram (Whole)", "hi": "लाल दाल (साबुत)", "mr": "लाल डाळ (संपूर्ण)"},
    "Unginned":           {"en": "Unginned", "hi": "अगिना हुआ", "mr": "अगिनलेला"},
    "Gram Whole / Kanta": {"en": "Gram Whole / Kanta", "hi": "चना साबुत / कांटा", "mr": "हरभरा संपूर्ण / कांटा"},
    "Deshi / Other":      {"en": "Deshi / Other", "hi": "देशी / अन्य", "mr": "देशी / इतर"},
    "Whole":              {"en": "Whole", "hi": "साबुत", "mr": "संपूर्ण"},
    "Yellow / Hybrid":    {"en": "Yellow / Hybrid", "hi": "पीला / हाइब्रिड", "mr": "पिवळा / हायब्रिड"},
    "White / Other":      {"en": "White / Other", "hi": "सफ़ेद / अन्य", "mr": "पांढरा / इतर"},
}

# Sub-mandi commodity translations
SUBMANDI_COMMODITIES = {
    "Soybean, Cotton, Tur":           {"en": "Soybean, Cotton, Tur", "hi": "सोयाबीन, कपास, अरहर", "mr": "सोयाबीन, कापूस, तूर"},
    "Wheat, Tur, Bengal Gram, Sesame": {"en": "Wheat, Tur, Bengal Gram, Sesame", "hi": "गेहूं, अरहर, चना, तिल", "mr": "गहू, तूर, हरभरा, तीळ"},
    "Soybean, Tur":                    {"en": "Soybean, Tur", "hi": "सोयाबीन, अरहर", "mr": "सोयाबीन, तूर"},
    "Soybean, Gram":                   {"en": "Soybean, Gram", "hi": "सोयाबीन, चना", "mr": "सोयाबीन, हरभरा"},
}

# Month abbreviation translations (for rainfall chart labels)
MONTH_ABBREV = {
    "May":       {"en": "May", "hi": "मई", "mr": "मे"},
    "June":      {"en": "Jun", "hi": "जून", "mr": "जून"},
    "July":      {"en": "Jul", "hi": "जुला", "mr": "जुलै"},
    "August":    {"en": "Aug", "hi": "अग", "mr": "ऑग"},
    "September": {"en": "Sep", "hi": "सितं", "mr": "सप्टे"},
    "October":   {"en": "Oct", "hi": "अक्टू", "mr": "ऑक्टो"},
    "November":  {"en": "Nov", "hi": "नवं", "mr": "नोव्हे"},
    "December":  {"en": "Dec", "hi": "दिसं", "mr": "डिसें"},
}

# Crop recommendation data — profitable crops by season/month
CROP_RECOMMENDATIONS = {
    "Kharif": {
        "en": "In Kharif season (June-October), the most profitable crops for Wardha are Soybean (₹6,265/Qtl modal price) and Cotton (₹7,500/Qtl). Tur/Arhar also commands a high price at ₹7,795/Qtl and is drought-resilient. If your current crop is failing, consider switching to Tur which tolerates moisture stress better.",
        "hi": "खरीफ मौसम (जून-अक्टूबर) में वर्धा की सबसे लाभदायक फसलें सोयाबीन (₹६,२६५/क्विं मॉडल मूल्य) और कपास (₹७,५००/क्विं) हैं। अरहर भी ₹७,७९५/क्विं पर उच्च मूल्य देता है और सूखा-सहनशील है। यदि आपकी वर्तमान फसल विफल हो रही है, तो अरहर में बदलने पर विचार करें जो नमी के तनाव को बेहतर ढंग से सहन करता है।",
        "mr": "खरीप हंगामात (जून-ऑक्टोबर) वर्धा जिल्ह्यातील सर्वाधिक नफेकारक पिके सोयाबीन (₹६,२६५/क्विं मॉडल भाव) आणि कापूस (₹७,५००/क्विं) आहेत. तूरही ₹७,७९५/क्विं या उच्च भावावर मिळतो आणि तो दुष्काळ-सहनशील आहे. तुमचे सध्याचे पीक अपयशी जात असल्यास, तूरकडे वळण्याचा विचार करा जो ओलाव्याच्या तणावाला अधिक चांगल्या प्रकारे सहन करतो."
    },
    "Rabi": {
        "en": "In Rabi season (November-March), Gram (₹6,175/Qtl) and Wheat (₹2,650/Qtl) are the main crops. Gram offers better returns. If soil moisture is limited after a poor monsoon, Gram is more tolerant than Wheat. Consider early sowing (mid-October) for best yields.",
        "hi": "रबी मौसम (नवंबर-मार्च) में चना (₹६,१७५/क्विं) और गेहूं (₹२,६५०/क्विं) मुख्य फसलें हैं। चना बेहतर रिटर्न देता है। खराब मानसून के बाद मिट्टी की नमी सीमित होने पर, चना गेहूं की तुलना में अधिक सहनशील है। बेहतर उपज के लिए जल्दी बुवाई (अक्टूबर के मध्य) पर विचार करें।",
        "mr": "रबी हंगामात (नोव्हेंबर-मार्च) हरभरा (₹६,१७५/क्विं) आणि गहू (₹२,६५०/क्विं) मुख्य पिके आहेत. हरभरा चांगला उत्पन्न देतो. खराब मानसूनानंतर मातीतील ओलावा मर्यादित असल्यास, हरभरा गहूपेक्षा अधिक सहनशील आहे. उत्तम उत्पन्नासाठी लवकर पेरणी (ऑक्टोबर मध्यभागी) याचा विचार करा."
    },
    "Summer": {
        "en": "In Summer (Feb-May), Sesamum (₹11,900/Qtl) gives the best returns in Wardha, the highest per-quintal price of any crop. It needs very little water, so it works well for summer sowing.",
        "hi": "ग्रीष्मकालीन मौसम (फरवरी-मई) में तिल (₹११,९००/क्विं) वर्धा में सबसे ज़्यादा कमाई वाली फसल है। इसे बहुत कम पानी चाहिए, तो गर्मियों की बुवाई के लिए अच्छा है।",
        "mr": "उन्हाळ्याच्या हंगामात (फेब्रुवारी-मे) तीळ (₹११,९००/क्विं) हे वर्धातील सर्वाधिक नफेकारक पीक आहे. याला खूप कमी पाण्याची गरज असते, त्यामुळे उन्हाळ्यातील पेरणीसाठी योग्य आहे."
    }
}

# Speech-to-text labels
STT_LABELS = {
    "start_listening":  {"en": "Start Listening", "hi": "सुनना शुरू करें", "mr": "ऐकून घेणे सुरू करा"},
    "stop_listening":   {"en": "Stop Listening", "hi": "सुनना बंद करें", "mr": "ऐकून घेणे थांबवा"},
    "listening":        {"en": "Listening... Speak now", "hi": "सुन रहे हैं... बोलें", "mr": "ऐकत आहे... बोला"},
    "speech_not_supported": {"en": "Speech recognition not supported in this browser. Use Chrome.", "hi": "इस ब्राउज़र में स्पीच रिकग्निशन समर्थित नहीं है। Chrome का उपयोग करें।", "mr": "या ब्राउझरमध्ये स्पीच रिकग्निशनला समर्थन नाही. Chrome वापरा."},
    "problem_voice":    {"en": "Describe your problem", "hi": "अपनी समस्या बताएं", "mr": "तुमची समस्या सांगा"},
    "solution_title":   {"en": "Recommended Solution", "hi": "अनुशंसित समाधान", "mr": "शिफारस केलेले उपाय"},
    "profit_tip_title": {"en": "Profit Tip", "hi": "मुनाफ़ा सुझाव", "mr": "नफा टीप"},

}

# Month number-to-key mapping for speech input
MONTH_KEYWORDS = {
    "en": {"january": "January", "february": "February", "march": "March", "april": "April", "may": "May", "june": "June", "july": "July", "august": "August", "september": "September", "october": "October", "november": "November", "december": "December"},
    "hi": {"जनवरी": "January", "फरवरी": "February", "मार्च": "March", "अप्रैल": "April", "मई": "May", "जून": "June", "जुलाई": "July", "अगस्त": "August", "सितंबर": "September", "अक्टूबर": "October", "नवंबर": "November", "दिसंबर": "December"},
    "mr": {"जानेवारी": "January", "फेब्रुवारी": "February", "मार्च": "March", "एप्रिल": "April", "मे": "May", "जून": "June", "जुलै": "July", "ऑगस्ट": "August", "सप्टेंबर": "September", "ऑक्टोबर": "October", "नोव्हेंबर": "November", "डिसेंबर": "December"}
}

LANGUAGE_NAMES = {"en": "English", "hi": "हिन्दी", "mr": "मराठी"}

# Devanagari numeral mapping (used for Hindi and Marathi)
_DEVANAGARI_DIGITS = str.maketrans('0123456789', '०१२३४५६७८९')


def num(value, lang):
    """
    Convert a number to Devanagari script for Hindi/Marathi.
    In English, returns the number as a string.
    Handles integers, floats, and strings with mixed content.
    """
    s = str(value)
    if lang == 'en':
        return s
    # Only translate if there are actual digits
    if any(c.isdigit() for c in s):
        return s.translate(_DEVANAGARI_DIGITS)
    return s


def t(key, lang):
    """Look up a UI string. Falls back to English, then to the raw key."""
    entry = UI.get(key, {})
    return entry.get(lang, entry.get("en", key))

def t_crop(crop, lang):
    entry = CROP_NAMES.get(crop, {})
    return entry.get(lang, entry.get("en", crop))

def t_month(month, lang):
    entry = MONTH_NAMES.get(month, {})
    return entry.get(lang, entry.get("en", month))

def t_status(status, lang):
    entry = STATUS_LABELS.get(status, {})
    return entry.get(lang, entry.get("en", status))

def t_variety(variety, lang):
    entry = VARIETY_NAMES.get(variety, {})
    return entry.get(lang, entry.get("en", variety))

def t_submandi_commodities(commodities, lang):
    entry = SUBMANDI_COMMODITIES.get(commodities, {})
    return entry.get(lang, entry.get("en", commodities))

def t_month_abbr(month, lang):
    entry = MONTH_ABBREV.get(month, {})
    return entry.get(lang, entry.get("en", month[:3]))

def t_stt(label, lang):
    entry = STT_LABELS.get(label, {})
    return entry.get(lang, entry.get("en", label))
