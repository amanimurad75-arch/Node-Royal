import streamlit as st
import requests
import time

# --- [1] التصميم الملكي (الأرجواني الملكي + الأبيض الثلجي) ---
st.set_page_config(page_title="NODE - Professional Studio", layout="wide")

st.markdown("""
    <style>
    /* خلفية أرجوانية ملكية سادة ونظيفة */
    .stApp { background-color: #4B0082; color: #FFFAFA; direction: rtl; }
    
    /* هيدر NODE الثلجي */
    .node-header {
        text-align: center; font-size: 80px; font-weight: 900;
        letter-spacing: 15px; color: #FFFAFA; 
        text-shadow: 3px 3px 15px rgba(0,0,0,0.4);
        padding: 30px 0;
    }
    
    /* صناديق العمل (الاستوديو) */
    .node-card {
        border: 2px solid #FFFAFA; border-radius: 20px;
        padding: 25px; background: rgba(255, 250, 250, 0.1);
        margin-bottom: 25px;
    }
    
    /* الأزرار الثلجية بالكتابة الأرجوانية */
    .stButton>button {
        background: #FFFAFA !important; color: #4B0082 !important;
        font-weight: 900; border-radius: 12px; border: none;
        height: 4em; width: 100%; transition: 0.3s ease;
    }

    /* ✅ الحل النهائي: الكتابة سوداء "مواطن" داخل البوكس الأبيض */
    .stTextArea textarea, .stTextInput input {
        background-color: #FFFFFF !important; 
        color: #000000 !important; /* كتابة سوداء واضحة جداً */
        border: 2px solid #FFFAFA !important; 
        text-align: right; direction: rtl; font-size: 18px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- [2] نظام تسجيل الدخول والخروج ---
if 'auth' not in st.session_state: st.session_state.auth = False

st.markdown("<div class='node-header'>NODE</div>", unsafe_allow_html=True)

col_sp, col_auth = st.columns([4, 1])
with col_auth:
    if not st.session_state.auth:
        if st.button("👤 دخول Google"): st.session_state.auth = True; st.rerun()
    else:
        st.markdown(f'<div style="border:2px solid #FFFAFA; padding:10px; border-radius:12px; text-align:center;">👑 <b>أماني مراد</b></div>', unsafe_allow_html=True)
        if st.button("تسجيل الخروج"): st.session_state.auth = False; st.rerun()

if st.session_state.auth:
    # --- [3] استوديو إنشاء الصور ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.subheader("🎨 استوديو التصميم المتكامل")
    prompt = st.text_area("وصفي مشهدكِ الإبداعي:", placeholder="اكتبي الوصف هنا (الخط سيظهر باللون الأسود)...")

    if st.button("🚀 بدء التوليد"):
        if prompt:
            status = st.empty()
            status.info("⏳ جاري سحب الإبداع...")
            url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed={int(time.time())}&model=flux"
            try:
                res = requests.get(url, timeout=50)
                if res.status_code == 200:
                    status.empty()
                    st.image(res.content, use_column_width=True)
                    st.download_button("📥 حفظ التصميم", data=res.content, file_name="node_art.png")
            except:
                status.error("❌ فشل الاتصال.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- [4] مربع الحوار العربي للفيديو ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.subheader("🎬 مركز التحريك والنطق")
    dialogue = st.text_area("اكتبي النص العربي للنطق:", placeholder="أهلاً بكِ أماني...")
    
    if st.button("✨ اعتماد الحوار"):
        if dialogue:
            st.success(f"✅ تم اعتماد النص العربي: '{dialogue}'")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.8; color:#FFFAFA;'>إشراف وتطوير الملكة: أماني مراد | NODE 2026</p>", unsafe_allow_html=True)
