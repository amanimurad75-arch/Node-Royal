import streamlit as st
import requests
from io import BytesIO

# --- إعدادات NODE الملكية ---
st.set_page_config(page_title="NODE", layout="wide")

# إعدادات نمط التطبيق للهواتف
st.markdown("""
    <style>
    .main { background-color: #2d0050; color: #f0f8ff; direction: rtl; }
    .hero-title {
        text-align: center; font-size: 50px; font-weight: bold;
        color: #f0f8ff; text-shadow: 0px 0px 15px rgba(255,255,255,0.5);
        padding: 10px;
    }
    .footer-box {
        background-color: rgba(106, 13, 173, 0.4);
        border: 2px solid #f0f8ff; border-radius: 15px;
        padding: 15px; margin-top: 10px; text-align: center;
    }
    .plus-icon { font-size: 40px; color: #ffd700; font-weight: bold; }
    .user-box { border: 1px solid white; border-radius: 10px; padding: 10px; background: #4b0082; text-align: center; }
    .stButton>button { background: #f0f8ff; color: #2d0050; font-weight: bold; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# نظام الدخول
if 'auth' not in st.session_state:
    st.session_state.auth = False

col_h1, col_h2 = st.columns([7, 3])
with col_h2:
    if st.session_state.auth:
        st.markdown('<div class="user-box">👤 <b>أماني مراد</b><br><small>amani.murad.75@gmail.com</small></div>', unsafe_allow_html=True)
    else:
        if st.button("🔴 دخول Gmail"):
            st.session_state.auth = True
            st.rerun()

st.markdown("<div class='hero-title'>NODE</div>", unsafe_allow_html=True)

if st.session_state.auth:
    tab1, tab2 = st.tabs(["📸 إنشاء صورة", "🎬 تحويل فيديو"])

    with tab1:
        prompt = st.text_input("صفي الصورة الثلجية:")
        if st.button("🚀 إنشاء"):
            img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed=8"
            st.image(img_url, use_column_width=True)
            st.markdown('<div class="footer-box"><div class="plus-icon">+</div><p>القياس: 1024x1024 HD<br>الحالة: صورة جاهزة للتحميل</p></div>', unsafe_allow_html=True)
            img_data = requests.get(img_url).content
            st.download_button("📥 حفظ الصورة", data=img_data, file_name="node.png")

    with tab2:
        up = st.file_uploader("ارفعي الصورة للتحويل:")
        if up:
            st.image(up, width=250)
            sz = st.selectbox("القياس:", ["9:16 (TikTok)", "16:9 (YouTube)", "1:1 (Insta)"])
            tm = st.selectbox("المدة:", ["5s", "10s", "20s"])
            if st.button("✨ ابدأ"):
                st.info("جاري التحويل...")
                st.markdown(f'<div class="footer-box"><div class="plus-icon">+</div><p>المدة: {tm}<br>القياس: {sz}</p></div>', unsafe_allow_html=True)
else:
    st.info("يرجى تسجيل الدخول")

st.caption("تطوير: أماني مراد - 2026")
