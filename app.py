import streamlit as st
import requests
import time

# --- [1] إعدادات الاستوديو (أرجواني ملكي + أبيض ثلجي) ---
st.set_page_config(page_title="NODE - Ultra Professional", layout="wide")

st.markdown("""
    <style>
    /* خلفية أرجوانية ملكية سادة */
    .stApp { background-color: #4B0082; color: #FFFAFA; direction: rtl; }
    
    /* هيدر NODE الثلجي */
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
    
    /* الأزرار الثلجية بالكتابة الأرجوانية */
    .stButton>button {
        background: #FFFAFA !important; color: #4B0082 !important;
        font-weight: 900; border-radius: 12px; border: none;
        height: 4em; width: 100%; transition: 0.3s;
    }

    /* ✅ حل نهائي: الكتابة سوداء "مواطن" داخل البوكس الأبيض */
    .stTextArea textarea, .stTextInput input {
        background-color: #FFFFFF !important; 
        color: #000000 !important; 
        border: 2px solid #FFFAFA !important; 
        text-align: right; direction: rtl; font-size: 18px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- [2] نظام تسجيل الدخول والخروج (ثابت) ---
if 'auth_node' not in st.session_state: st.session_state.auth_node = False

st.markdown("<div class='node-header'>NODE</div>", unsafe_allow_html=True)

col_empty, col_auth_box = st.columns([4, 1])
with col_auth_box:
    if not st.session_state.auth_node:
        if st.button("👤 دخول Google"): st.session_state.auth_node = True; st.rerun()
    else:
        st.markdown(f'<div style="border:2px solid #FFFAFA; padding:10px; border-radius:12px; text-align:center;">👑 <b>أماني مراد</b></div>', unsafe_allow_html=True)
        if st.button("تسجيل الخروج"): st.session_state.auth_node = False; st.rerun()

if st.session_state.auth_node:
    # --- [3] استوديو إنشاء الصور HD ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.subheader("🎨 استوديو التصميم المتكامل")
    prompt = st.text_area("وصفي مشهدكِ الإبداعي:", placeholder="اكتبي الوصف هنا (الخط سيظهر باللون الأسود)...")

    st.write("#### 📏 أبعاد الإنتاج المعتمدة (Fix 3):")
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("📱 9:16 (Tall)"): st.session_state.dims = (1024, 1792)
    with c2: 
        if st.button("🔳 1:1 (Square)"): st.session_state.dims = (1024, 1024)
    with c3: 
        if st.button("📺 16:9 (Wide)"): st.session_state.dims = (1792, 1024)

    w, h = st.session_state.get('dims', (1024, 1024))
    
    if st.button("🚀 بدء التوليد"):
        if prompt:
            msg = st.empty()
            msg.info("⏳ جاري سحب الإبداع من السيرفر...")
            url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width={w}&height={h}&seed={int(time.time())}&model=flux"
            try:
                res = requests.get(url, timeout=50)
                if res.status_code == 200 and len(res.content) > 15000:
                    msg.empty()
                    st.image(res.content, use_column_width=True)
                    st.download_button("📥 حفظ التصميم", data=res.content, file_name="node_art.png")
                else:
                    msg.error("⚠️ السيرفر مشغول، حاولي مرة ثانية يا أماني.")
            except:
                msg.error("❌ فشل الاتصال بالسيرفر.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- [4] مركز التحريك ونطق الفيديو (بوكس الحوار العربي) ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.subheader("🎬 مركز التحريك ونطق الفيديو")
    up = st.file_uploader("ارفعي صورة الشخصية هنا:", type=["png", "jpg"])
    
    if up:
        st.image(up, width=280)
        # ميزة بوكس الحوار العربي الثابتة
        st.write("#### 💬 إعدادات الحوار والنطق:")
        dialogue_text = st.text_area("اكتبي النص الذي ستنطقه الشخصية بالعربي:", placeholder="مثال: أهلاً بكِ في NODE...")
        motion_type = st.selectbox("😊 اختر نمط الحركة:", ["تضحك وتتحدث", "تغمز وتتكلم", "نطق هادئ"])
        
        if st.button("✨ توليد الفيديو الناطق"):
            if dialogue_text:
                st.success(f"✅ تم اعتماد النص العربي: '{dialogue_text}'")
            else:
                st.warning("⚠️ يرجى كتابة نص النطق أولاً.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.8; color:#FFFAFA;'>إشراف وتطوير الملكة: أماني مراد | NODE 2026</p>", unsafe_allow_html=True)
