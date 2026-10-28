import streamlit as st

st.set_page_config(page_title="रेलवे परिचालन नियम क्विज़", page_icon="🚂", layout="centered")

# 6 यूज़र्स का लॉगिन डेटाबेस (अब सभी का पासवर्ड सिर्फ 1 है)
USER_CREDENTIALS = {
    "user1": "1",
    "user2": "1",
    "user3": "1",
    "user4": "1",
    "user5": "1",
    "user6": "1"
}

# 1 से 54 तक के चुनिंदा प्रश्न
QUESTIONS = [
    {"id": 1, "question": "पॉइन्ट इन्डीकेटर सीधी लाइन के लिए सेट हो तो रात में कौन सी बत्ती बताएगा?", "options": ["हरी बत्ती", "सफेद बत्ती", "लाल बत्ती", "पीली बत्ती"], "correct": "सफेद बत्ती"},
    {"id": 2, "question": "ब्लॉक सेक्शन कमिट बोर्ड कौन से स्टेशन पर होता है?", "options": ["बी क्लास डबल लाइन बहुसंकेती", "ए क्लास सिंगल लाइन", "सी क्लास स्टेशन", "डी क्लास स्टेशन"], "correct": "बी क्लास डबल लाइन बहुसंकेती"},
    {"id": 3, "question": "पॉइन्ट इन्डीकेटर हरी बत्ती बता रहा हो तो वह किस लाइन के लिए सेट है?", "options": ["सीधी लाइन", "लूप लाइन", "मुख्य लाइन", "टर्न आउट"], "correct": "टर्न आउट"},
    {"id": 4, "question": "स्टेशन सेक्शन कौन से क्लास के स्टेशन पर होता है?", "options": ["ए क्लास", "सी क्लास", "बी क्लास", "डी क्लास"], "correct": "बी क्लास"},
    {"id": 5, "question": "जो लाइन सिगनलों से नियंत्रित होती है, उसे कौन सी लाइन कहते हैं?", "options": ["शंट लाइन", "रनिंग लाइन", "साइडिंग लाइन", "डेड एंड लाइन"], "correct": "रनिंग लाइन"},
    {"id": 6, "question": "दिन का समय कब से कब तक माना जाता है?", "options": ["शाम 6 बजे से सुबह 6 बजे तक", "सुबह 6 बजे से शाम 6 बजे तक", "सूर्यास्त से सूर्योदय तक", "सूर्योदय से सूर्यास्त तक"], "correct": "सूर्योदय से सूर्यास्त तक"},
    {"id": 7, "question": "आई.बी.एस. (IBS) कौन से सेक्शन में होता है?", "options": ["सिंगल लाइन मैकेनिकल सेक्शन", "नॉन-इंटरलॉक्ड सेक्शन", "डबल लाइन रंगीन बत्ती", "केवल उपनगरीय सेक्शन"], "correct": "डबल लाइन रंगीन बत्ती"},
    {"id": 8, "question": "दो संकेतीय सिग्नल व्यवस्था वाले स्टेशन पर लाइन क्लीयर देने की पर्याप्त दूरी कितनी है?", "options": ["120 मी.", "400 मी.", "180 मी.", "250 मी."], "correct": "400 मी."},
    {"id": 9, "question": "बहु संकेतीय सिग्नल व्यवस्था वाले स्टेशन पर सिग्नल ऑफ करने की पर्याप्त दूरी कितनी है?", "options": ["120 मी.", "400 मी.", "180 मी.", "500 मी."], "correct": "120 मी."},
    {"id": 10, "question": "पश्चिम रेलवे एवं उत्तर पश्चिम रेलवे पर अधिकृत अधिकारी कौन हैं?", "options": ["महाप्रबंधक (GM)", "मंडल रेल प्रबंधक (DRM)", "मुख्य सुरक्षा आयुक्त", "परिचालन प्रबंधक (मु.)"], "correct": "परिचालन प्रबंधक (मु.)"},
    {"id": 11, "question": "अनुमोदित विशेष अनुदेश किसके द्वारा जारी किए जाते हैं?", "options": ["रेलवे बोर्ड", "महाप्रबंधक", "सी आर एस (CRS)", "मुख्य परिचालन प्रबंधक"], "correct": "सी आर एस (CRS)"},
    {"id": 12, "question": "क्या पॉइन्ट इन्डीकेटर एक सिगनल है?", "options": ["हाँ, यह एक स्थिर सिगनल है", "नहीं", "हाँ, रात के समय सिगनल है", "केवल शंटिंग सिगनल है"], "correct": "नहीं"},
    {"id": 13, "question": "रेलवे में कितने प्रकार के ब्लॉक स्टेशन होते हैं?", "options": ["3", "2", "4", "5"], "correct": "3"},
    {"id": 14, "question": "जहाँ सड़क और रेलवे लाइन एक दूसरे को समान स्तर पर पार करती हैं, उस स्थान को क्या कहते हैं?", "options": ["OVERBRIDGE", "अंडरпас", "सबवे", "समपार (Level Crossing)"], "correct": "समपार (Level Crossing)"},
    {"id": 15, "question": "रात का समय कब से कब तक माना जाता है?", "options": ["शाम 8 बजे से सुबह 6 बजे तक", "सूर्योदय से सूर्यास्त तक", "सूर्यास्त से सूर्योदय तक", "रात 10 बजे से सुबह 5 बजे तक"], "correct": "सूर्यास्त से सूर्योदय तक"},
    {"id": 16, "question": "क्या ट्रेलिंग पॉइन्ट आती हुई गाड़ी की दिशा बदल सकता है?", "options": ["हाँ, गाड़ी के पहियों के दबाव से", "नहीं", "हाँ, विशेष अनुमति पर", "केवल मालगाड़ी के मामले में हाँ"], "correct": "नहीं"},
    {"id": 17, "question": "ब्लॉक सेक्शन में तूफान आ जाए, तो लोको पायलट गाड़ी को कहाँ खड़ी करेगा?", "options": ["सुरक्षित स्थान पर", "तुरंत बीच ट्रैक पर", "अगले स्टेशन के होम सिगनल पर", "पुल के ठीक ऊपर"], "correct": "सुरक्षित स्थान पर"},
    {"id": 18, "question": "एनीमोमीटर किस बात की सूचना देता है?", "options": ["तापमान में वृद्धि", "वर्षा की तीव्रता", "वायु दाब", "हवा का वेग"], "correct": "हवा का वेग"},
    {"id": 19, "question": "रेलवे संचालन के लिए रेलवे में मुख्य रूप से कितने प्रकार के सिगनल होते हैं?", "options": ["2", "3", "4", "5"], "correct": "4"}
]

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

if not st.session_state.logged_in:
    st.title("🚂 रेलवे परिचालन नियम - लॉगिन पोर्टल")
    
    # .strip().lower() से स्पेस की गलती और छोटे-बड़े अक्षरों का झंझट खत्म हो जाएगा
    username_input = st.text_input("यूज़र आईडी (User ID)").strip().lower()
    password_input = st.text_input("पासवर्ड (Password)", type="password").strip()
    
    if st.button("लॉगिन करें", use_container_width=True):
        if username_input in USER_CREDENTIALS and USER_CREDENTIALS[username_input] == password_input:
            st.session_state.logged_in = True
            st.session_state.username = username_input
            st.rerun()
        else:
            st.error("❌ गलत यूज़र आईडी या पासवर्ड!")
else:
    st.title("🎯 परिचालन नियम ऑब्जेक्टिव टेस्ट")
    st.sidebar.success(f"👤 लॉग इन: {st.session_state.username.upper()}")
    if st.sidebar.button("लॉग आउट"):
        st.session_state.logged_in = False
        st.session_state.quiz_submitted = False
        st.rerun()

    user_answers = {}
    for idx, q in enumerate(QUESTIONS):
        st.markdown(f"**प्रश्न {idx + 1}: {q['question']}**")
        user_answers[q['id']] = st.radio(f"Q_{q['id']}", options=q['options'], key=f"q_{q['id']}", label_visibility="collapsed")
        st.write("---")
        
    if not st.session_state.quiz_submitted:
        if st.button("अपना स्कोर और रिजल्ट देखें", type="primary", use_container_width=True):
            current_score = sum(1 for q in QUESTIONS if user_answers[q['id']] == q['correct'])
            st.session_state.score = current_score
            st.session_state.quiz_submitted = True
            st.rerun()

    if st.session_state.quiz_submitted:
        st.balloons()
        st.success(f"🎉 आपका कुल स्कोर: {st.session_state.score} / {len(QUESTIONS)}")
        if st.button("दोबारा टेस्ट दें", use_container_width=True):
            st.session_state.quiz_submitted = False
            st.rerun()
