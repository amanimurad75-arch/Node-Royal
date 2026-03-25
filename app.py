import streamlit as st
import requests
import time

# --- [1] الواجهة الأرجوانية الملكية (الخلفية أرجواني + الخط ثلجي) ---
st.set_page_config(page_title="NODE - Royal Purple", layout="wide")

st.markdown("""
    <style>
    /* الخلفية أرجواني ملكي بالكامل */
    .stApp { background-color: #4B0082; color: #FFFAFA; direction: rtl; }
    
    /* هيدر NODE بالأبيض الثلجي */
    .node-header {
        text-align: center; font-size: 75px; font-weight: 900;
        letter-spacing: 15px; color: #FFFAFA; 
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
        padding: 40px 0;
    }
    
    /* صناديق العمل (Cards) شفافة بحدود بيضاء ثلجية لتبدو ملكية */
    .node-card {
        border: 2px solid #FFFAFA; border-radius: 20px;
        padding: 30px; background: rgba(255, 250, 250, 0.1);
        margin-bottom: 30px;
    }
    
    /* الأزرار بالأبيض الثلجي والكتابة بالأرجواني */
    .stButton>button {
        background: #FFFAFA !important; color: #4B0082 !important;
        font-weight: 900; border-radius: 12px; border: none;
        height: 3.8em; width: 100%; transition: 0.4s ease;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px #FFFAFA; }

    /* بوكس الحوار العربي */
    .stTextInput input, .stTextArea textarea {
        background-color: rgba(255, 250, 250, 0.2) !important; color: #FFFAFA !important;
        border: 2px solid #FFFAFA !important; text-align: right; 
        direction: rtl; font-size: 18px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- [2] ميزة تسجيل الدخول والخروج (ثابتة - لن تُحذف) ---
if 'auth_active' not in st.session_state: st.session_state.auth_active = False

st.markdown("<div class='node-header'>NODE</div>", unsafe_allow_html=True)

col_empty, col_log = st.columns([4, 1])
with col_log:
    if not st.session_state.auth_active:
        if st.button("👤 دخول Google"): st.session_state.auth_active = True; st.rerun()
    else:
        st.markdown(f'<div style="border:2px solid #FFFAFA; padding:10px; border-radius:12px; text-align:center;">👑 <b>أماني مراد</b></div>', unsafe_allow_html=True)
        if st.button("خروج"): st.session_state.auth_active = False; st.rerun()

if st.session_state.auth_active:
    # --- [3] استوديو الصور (حل السيرفر + القياسات) ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.write("### 🎨 استوديو التصميم (الخلفية أرجواني)")
    prompt = st.text_area("وصفي إبداعكِ القادم:", placeholder="اكتبي وصف الصورة هنا...")

    st.write("#### 📏 القياسات (Fix 3):")
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("📱 Tall (9:16)"): st.session_state.v_size = (1024, 1792)
    with c2: 
        if st.button("🔳 Square (1:1)"): st.session_state.v_size = (1024, 1024)
    with c3: 
        if st.button("📺 Wide (16:9)"): st.session_state.v_size = (1792, 1024)

    w, h = st.session_state.get('v_size', (1024, 1024))
    
    if st.button("🚀 توليد وعرض الصورة"):
        if prompt:
            ld = st.empty()
            ld.info("⏳ جاري سحب الصورة من السيرفر...")
            img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width={w}&height={h}&seed={int(time.time())}&model=flux"
            try:
                res = requests.get(img_url, timeout=50)
                if res.status_code == 200 and len(res.content) > 15000:
                    ld.empty()
                    st.image(res.content, use_column_width=True)
                    st.download_button("📥 حفظ العمل", data=res.content, file_name="node_purple.png")
                else:
                    ld.error("❌ السيرفر مشغول، حاولي مرة ثانية.")
            except:
                ld.error("❌ فشل الاتصال.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- [4] مركز التحريك و (بوكس الحوار العربي الثابت) ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.write("### 🎬 مركز التحريك ونطق الفيديو")
    up_img = st.file_uploader("ارفعي صورة الشخصية هنا:", type=["png", "jpg"])
    
    if up_img:
        st.image(up_img, width=280)
        st.write("#### 💬 إعدادات الحوار العربي:")
        # بوكس الحوار الثابت اللي طلبتيه
        voice_text = st.text_area("اكتبي النص العربي الذي ستنطقه الشخصية:", placeholder="أهلاً بكِ أماني...")
        motion_style = st.selectbox("😊 تعبير الوجه:", ["تضحك وتتحدث", "تغمز وتتكلم", "نطق هادئ"])
        
        if st.button("✨ إنتاج فيديو ناطق"):
            if voice_text:
                st.success(f"✅ تم اعتماد الحوار: '{voice_text}'")
            else:
                st.warning("⚠️ اكتبي النص العربي أولاً.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.8; color:#FFFAFA;'>إشراف وتطوير الملكة: أماني مراد | NODE 2026</p>", unsafe_allow_html=True)
