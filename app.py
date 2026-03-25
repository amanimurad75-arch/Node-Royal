import streamlit as st
import requests
import time

# --- [1] الهوية البصرية الملكية (ثابتة تماماً) ---
st.set_page_config(page_title="NODE - Professional Studio", layout="wide")

st.markdown("""
    <style>
    /* خلفية أرجوانية ملكية سادة */
    .stApp { background-color: #4B0082; color: #FFFAFA; direction: rtl; }
    
    /* هيدر NODE الثلجي الكبير */
    .node-header {
        text-align: center; font-size: 80px; font-weight: 900;
        letter-spacing: 15px; color: #FFFAFA; 
        text-shadow: 3px 3px 15px rgba(0,0,0,0.4);
        padding: 30px 0;
    }
    
    /* صناديق العمل (Cards) بحدود ثلجية */
    .node-card {
        border: 2px solid #FFFAFA; border-radius: 20px;
        padding: 25px; background: rgba(255, 250, 250, 0.1);
        margin-bottom: 25px;
    }
    
    /* ✅ الخط أسود "مواطن" داخل البوكس الأبيض (إلزامي) */
    .stTextArea textarea, .stTextInput input {
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
        border: 2px solid #FFFAFA !important; 
        text-align: right; direction: rtl; font-size: 18px !important;
    }

    /* الأزرار الثلجية بالكتابة الأرجوانية */
    .stButton>button {
        background: #FFFAFA !important; color: #4B0082 !important;
        font-weight: 900; border-radius: 12px; border: none;
        height: 3.5em; width: 100%; transition: 0.3s ease;
    }
    </style>
    """, unsafe_allow_html=True)

# --- [2] نظام تسجيل الدخول والخروج (تثبيت كامل) ---
if 'auth' not in st.session_state: st.session_state.auth = False

st.markdown("<div class='node-header'>NODE</div>", unsafe_allow_html=True)

# قسم تسجيل الدخول في الأعلى
col_empty, col_log = st.columns([4, 1])
with col_log:
    if not st.session_state.auth:
        if st.button("👤 تسجيل الدخول"): st.session_state.auth = True; st.rerun()
    else:
        st.markdown(f'<div style="border:2px solid #FFFAFA; padding:10px; border-radius:12px; text-align:center;">👑 <b>أماني مراد</b></div>', unsafe_allow_html=True)
        if st.button("🚪 تسجيل الخروج"): st.session_state.auth = False; st.rerun()

if st.session_state.auth:
    # --- [3] ميزة نقل الملفات (الميزة الجديدة لحالها) ---
    with st.expander("📥 ميزة جديدة: نقل ملفات من الموقع السابق لحسابكِ الجديد"):
        st.markdown('<div class="node-card">', unsafe_allow_html=True)
        st.file_uploader("انقلي صوركِ أو ملفاتكِ هنا:", accept_multiple_files=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- [4] استوديو التصميم المتكامل (ثابت مع إضافة مدة العرض) ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.write("### 🎨 استوديو التصميم المتكامل")
    prompt = st.text_area("وصفي مشهدكِ الإبداعي القادم:", placeholder="فتاة صغيرة كرتونية ثلاثية الأبعاد...")

    # ✅ إضافة ميزة: مدة عرض الصورة أو الفيديو
    st.write("#### ⏱️ مدة عرض العمل:")
    duration = st.select_slider("حددي مدة عرض الصورة أو الفيديو (بالثواني):", options=[3, 5, 10, 15, 30, 60], value=5)

    # ✅ أزرار القياسات (Fix 3) - ثابتة ولن تحذف
    st.write("#### 📏 اختيار القياس (Fix 3):")
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("📱 Tall (9:16)"): st.session_state.res = (1024, 1792)
    with c2: 
        if st.button("🔳 Square (1:1)"): st.session_state.res = (1024, 1024)
    with c3: 
        if st.button("📺 Wide (16:9)"): st.session_state.res = (1792, 1024)

    if st.button("🚀 بدء التوليد وعرض الصورة HD"):
        if prompt:
            st.info(f"⏳ جاري التوليد.. سيتم العرض لمدة {duration} ثوانٍ.")
            # منطق التوليد هنا
    st.markdown('</div>', unsafe_allow_html=True)

    # --- [5] مركز التحريك ونطق الفيديو (ثابت وبدون حذف) ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.write("### 🎬 مركز التحريك ونطق الفيديو")
    # ✅ بوكس تحميل الصورة للتحريك
    st.file_uploader("ارفعي صورة الشخصية هنا لتحريكها:", type=["png", "jpg"])
    
    # بوكس الحوار العربي (ثابت)
    st.write("#### 💬 إعدادات الحوار والنطق:")
    speech = st.text_area("اكتبي النص العربي الذي ستنطقه الشخصية:", placeholder="أهلاً بكِ في NODE يا أماني...")
    
    if st.button("✨ اعتماد الحوار للفيديو"):
        if speech:
            st.success(f"✅ تم ضبط النطق للعرض لمدة {duration} ثوانٍ.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- [6] تذييل الصفحة الملكي ---
st.markdown("<p style='text-align:center; opacity:0.8; color:#FFFAFA;'>إشراف وتطوير الملكة: أماني مراد | NODE 2026</p>", unsafe_allow_html=True)
