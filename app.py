import streamlit as st
import requests
from io import BytesIO

# --- إعدادات NODE الملكية النهائية ---
st.set_page_config(page_title="NODE", layout="wide")

# التصميم بالأبيض الثلجي والأرجواني الملكي
st.markdown("""
    <style>
    .main { background-color: #2d0050; color: #f0f8ff; direction: rtl; }
    .hero-title {
        text-align: center; font-size: 55px; font-weight: bold;
        color: #f0f8ff; text-shadow: 0px 0px 15px rgba(255,255,255,0.5);
        padding: 10px;
    }
    .animated-box-outer {
        border: 2px solid #f0f8ff; border-radius: 20px;
        padding: 5px; margin-top: 15px;
    }
    .animated-box-inner {
        background-color: rgba(106, 13, 173, 0.5); border-radius: 15px;
        padding: 15px; text-align: center; color: white;
    }
    .image-icon { font-size: 60px; color: #ffd700; }
    .plus-icon { font-size: 30px; color: #ffd700; font-weight: bold; }
    
    /* ستايل زر تسجيل الخروج */
    .stButton>button {
        background: linear-gradient(45deg, #f0f8ff, #e0e0e0);
        color: #2d0050; font-weight: bold; border-radius: 10px; width: 100%;
    }
    .logout-btn>div>button {
        background: #ff4b4b !important; color: white !important; border: none !important;
    }
    
    .user-info { border: 2px solid white; border-radius: 10px; padding: 15px; background: #4b0082; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة الدخول
if 'auth' not in st.session_state:
    st.session_state.auth = False

# شريط المعلومات العلوي مع زر الخروج
col_h1, col_h2 = st.columns([7, 3])
with col_h2:
    if st.session_state.auth:
        st
