import streamlit as st
import requests
from io import BytesIO

# --- إعدادات NODE الملكية ---
st.set_page_config(page_title="NODE - Royal Edition", layout="wide")

# التصميم بالأرجواني الملكي مع عناصر واجهة 1044.jpg
st.markdown("""
    <style>
    .stApp {
        background-color: #1a0033;
        background-image: radial-gradient(circle at center, #2d0050 0%, #1a0033 100%);
        color: #f0f8ff;
        direction: rtl;
    }
    
    /* كلمة NODE في الأعلى بوضوح */
    .hero-section {
        text-align: center; padding-top: 2vh; margin-bottom: 20px;
    }
    .node-title {
        font-size: 70px; font-weight: bold; color: #f0f8ff;
        text-shadow: 0px 0px 20px rgba(255,255,255,0.6);
        letter-spacing: 10px;
    }

    /* تنسيق الكروت الرسومية والمقترحات */
    .card-style {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(240, 248, 255, 0.2);
        border-radius: 20px; padding: 15px; margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }
    
    /* شريط البحث السفلي مثل 1044.jpg */
    .stTextInput input {
        background-color: rgba(255,255,255,0.1) !important;
        color: white !important; border-radius: 30px !important;
        border: 1px solid #f0f8ff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- الهيدر ---
st.markdown('<div class="hero-section"><div class="node-title">NODE</div></div>', unsafe_allow_html=True)

# --- منطقة المستخدم ---
col_u1, col_u2 = st.columns([8, 2])
with col_u2:
    st.markdown('<div style="border:1px solid white; border-radius:15px; padding:10px; text-align:center;">👤 أماني مراد</div>', unsafe_allow_html=True)

# --- لوحة التحكم في القياسات والمده (مسترجعة بالكامل) ---
st.markdown("### ⚙️ إعدادات الإخراج الملكي")
col_p1, col_p2, col_p3 = st.columns(3)
with col_p1:
    ratio = st.selectbox("قياس الصورة/الفيديو:", ["1:1 (مربع)", "16:9 (عرضي)", "9:16 (طولي)"])
with col_p2:
    duration = st.select_slider("مدة الفيديو (ثواني):", options
