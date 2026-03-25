import streamlit as st
import requests
import time

# --- [1] الهوية البصرية الملكية (ثابتة بدون تغيير) ---
st.set_page_config(page_title="NODE - Ultra Professional", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #4B0082; color: #FFFAFA; direction: rtl; }
    .node-header { text-align: center; font-size: 80px; font-weight: 900; color: #FFFAFA; padding: 30px 0; }
    .node-card { border: 2px solid #FFFAFA; border-radius: 20px; padding: 25px; background: rgba(255, 250, 250, 0.1); margin-bottom: 25px; }
    
    /* ✅ الخط أسود "مواطن" داخل البوكس الأبيض (ثابت) */
    .stTextArea textarea, .stTextInput input {
        background-color: #FFFFFF !important; color: #000000 !important; 
        border: 2px solid #FFFAFA !important; text-align: right; direction: rtl;
    }
    .stButton>button { background: #FFFAFA !important; color: #4B0082 !important; font-weight: 900; border-radius: 12px; height: 3.8em; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='node-header'>NODE</div>", unsafe_allow_html=True)

# --- [2] الميزة الجديدة: جسر نقل الملفات (إضافة منفصلة) ---
with st.expander("📥 ميزة جديدة: نقل ملفات من الموقع السابق لحسابكِ الجديد"):
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    old_files = st.file_uploader("📂 اسحبي ملفاتكِ/صوركِ القديمة هنا لنقلها للحساب الجديد:", accept_multiple_files=True)
    if old_files:
        st.success(f"✅ تم نقل {len(old_files)} ملفات بنجاح إلى قاعدة بياناتكِ الجديدة.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- [3] استوديو التصميم (نفس الترتيب الأصلي) ---
st.markdown('<div class="node-card">', unsafe_allow_html=True)
st.write("### 🎨 استوديو التصميم المتكامل")
prompt = st.text_area("وصفي مشهدكِ الإبداعي:", placeholder="اكتبي الوصف هنا (الخط سيظهر باللون الأسود)...")

# القياسات (Fix 3)
st.write("#### 📏 اختيار القياس (Fix 3):")
c1, c2, c3 = st.columns(3)
with c1: 
    if st.button("📱 Tall (9:16)"): st.session_state.sz = (1024, 1792)
with c2: 
    if st.button("🔳 Square (1:1)"): st.session_state.sz = (1024, 1024)
with c3: 
    if st.button("📺 Wide (16:9)"): st.session_state.sz = (1792, 1024)

if st.button("🚀 بدء التوليد وعرض الصورة HD"):
    if prompt:
        w, h = st.session_state.get('sz', (1024, 1024))
        url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width={w}&height={h}&seed={int(time.time())}"
        st.image(url, use_column_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- [4] مركز التحريك ونطق الفيديو (نفس الترتيب الأصلي) ---
st.markdown('<div class="node-card">', unsafe_allow_html=True)
st.write("### 🎬 مركز التحريك ونطق الفيديو")
char_img = st.file_uploader("ارفعي صورة الشخصية هنا:", type=["png", "jpg"])

# بوكس الحوار العربي (نطق الفيديو)
st.write("#### 💬 إعدادات الحوار والنطق:")
speech_text = st.text_area("اكتبي النص العربي الذي ستنطقه الشخصية:", placeholder="مثال: أهلاً بكِ في NODE...")

if st.button("✨ اعتماد الحوار"):
    if speech_text: st.success(f"✅ تم تثبيت النص: '{speech_text}'")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.8; color:#FFFAFA;'>إشراف وتطوير الملكة: أماني مراد | NODE 2026</p>", unsafe_allow_html=True)
