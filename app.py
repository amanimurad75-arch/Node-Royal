import streamlit as st
import requests
import time

# --- [الكتلة 1]: الإعدادات البصرية الثابتة ---
st.set_page_config(page_title="NODE - Ultra Professional", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; direction: rtl; }
    .node-header { text-align: center; font-size: 60px; font-weight: 900; letter-spacing: 12px; padding: 20px; }
    .node-card {
        border: 1px solid rgba(255,255,255,0.1); border-radius: 15px;
        padding: 25px; background: rgba(255,255,255,0.03); margin-bottom: 25px;
    }
    .auth-box { border: 1px solid white; padding: 10px; border-radius: 8px; background: rgba(0,0,0,0.5); text-align: center; }
    .stButton>button { background: #ffffff; color: #000000; font-weight: bold; border-radius: 8px; width: 100%; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- [الكتلة 2]: نظام تسجيل الدخول (Gmail) - ثابت ---
if 'is_
