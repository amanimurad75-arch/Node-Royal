import streamlit as st
import requests
from io import BytesIO

# --- إعدادات NODE الملكية الفاخرة ---
st.set_page_config(page_title="NODE", layout="wide")

# التصميم بالأبيض الثلجي والأرجواني الاحترافي (تدرج Grok الفاخر)
st.markdown("""
    <style>
    /* خلفية NODE الفاخرة: تدرج أرجواني عميق مع شبكة Grok العصبية (Neural Net Background) */
    .stApp {
        background: radial-gradient(circle at center, #2d0050 0%, #1a0033 100%),
                    url('https://cdn.pixabay.com/photo/2021/08/25/11/49/data-center-6573105_1280.png') repeat !important;
        color: #f0f8ff; /* الأبيض الثلجي */
        direction: rtl;
        background-blend-mode: overlay;
    }
    
    /* عنوان NODE بالأبيض الثلجي اللامع */
    .hero-title {
        text-align: center; font-size: 55px; font-weight: bold;
        color: #f0f8ff; text-shadow: 0px 0px 15px rgba(255,255,255,0.7);
        padding: 20px; margin-bottom: 10px;
    }

    /* البوكسات الاحترافية بإطار ثلجي (grok-style panels) */
    .node-box {
        background: rgba(45, 0, 80, 0.6);
        border: 2px solid #f0f8ff; border-radius: 20px;
        padding: 20px; margin-top: 20px; text-align: center;
        backdrop-filter: blur(5px);
    }
    .plus-icon { font-size: 35px; color: #ffd700; font-weight: bold; }

    /* تنسيق أزرار التابلت الاحترافية */
    .stButton>button {
        background: linear-gradient(45deg, #f0f8ff, #e0e0e0);
        color: #1a0033; font-weight: bold; border-radius: 12px; height: 3.5em;
    }
    .user-card { border: 2px solid white; border-radius: 12px; padding: 10px; background: rgba(75, 0, 130, 0.8); text-align: center; }
    
    </style>
    """, unsafe_allow_html=True)

# نظام الدخول والخروج
if 'auth' not in st.session_state:
    st.session_state.auth = False

col_h1, col_h2 = st.columns([7, 3])
with col_h2:
    if st.session_state.auth:
        st.markdown('<div class="user-card">👤 <b>أماني مراد</b><br><small>amani.murad.75@gmail.com</small></div>', unsafe_allow_html=True)
        if st.button("🚪 تسجيل الخروج"):
            st.session_state.auth = False
