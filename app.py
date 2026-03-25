import streamlit as st
import requests
from io import BytesIO
import time # مكتبة لإدارة الانتظار

# --- إعدادات NODE الملكية (talking head update) ---
st.set_page_config(page_title="NODE - Professional Talking Head", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #2d0050; color: #f0f8ff; direction: rtl; }
    .hero-title {
        text-align: center; font-size: 60px; font-weight: bold;
        color: #f0f8ff; text-shadow: 0px 0px 20px rgba(255,255,255,0.7);
        padding: 20px;
    }
    .node-box {
        border: 2px solid #f0f8ff; border-radius: 20px;
        background: rgba(255, 255, 255, 0.05); padding: 20px; margin-top: 20px;
        backdrop-filter: blur(10px);
    }
    .stButton>button {
        background: linear-gradient(45deg, #f0f8ff, #e0e0
        
