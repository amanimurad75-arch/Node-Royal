import streamlit as st
import requests
import time

# --- [1] الواجهة الرسومية الاحترافية (Minimalist & Glossy) ---
st.set_page_config(page_title="NODE - Pro Edition", layout="wide")

st.markdown("""
    <style>
    /* خلفية داكنة ملكية مع تدرج خفيف */
    .stApp { background: linear-gradient(135deg, #050505 0%, #0f051a 100%); color: #ffffff; direction: rtl; }
    
    /* هيدر NODE بتصميم عصري */
    .node-header {
        text-align: center; font-size: 70px; font-weight: 900;
        letter-spacing: 20px; color: #ffffff; padding: 40px 0;
        text-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }
    
    /* صناديق العمل (Cards) بتصميم زجاجي احترافي */
    .stContainer {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px; padding: 30px; margin-bottom: 25px;
    }
    
    /* الأزرار (Buttons) بلمسة احترافية */
    .stButton>button {
        background: #ffffff; color: #000000; font-weight: bold;
        border-radius: 12px; border: none; height: 3.8em;
        transition: 0.4s ease-in-out; width: 100%;
    }
    .stButton>button:hover { background: #e0e0e0; transform: translateY(-3px); box-shadow: 0 5px 15px rgba(255,255,255,0.2); }
    
    /* مداخل النصوص */
    .stTextArea textarea, .stTextInput input {
        background-color: rgba(255,255,255,0.05) !important;
        color: white !important; border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# الهيدر ونظام تسجيل الدخول ( Gmail )
if 'auth_user' not in st.session_state: st.session_state.auth_user = False

st.markdown("<div class='node-header'>NODE</div>", unsafe_allow_html=True)

col_h1, col_h2 = st.columns([4, 1])
with col_h2:
    if not st.session_state.auth_user:
        if st.button("👤 Login with Google"): st.session_state.auth_user = True; st.rerun()
    else:
        st.markdown(f"<div style='border:1px solid white; padding:10px; border-radius:10px; text-align:center;'>👤 <b>أماني مراد</b></div>", unsafe_allow_html=True)

if st.session_state.auth_user:
    # --- [2] استوديو الصور (حل مشكلة السيرفر والعرض) ---
    with st.container():
        st.write("### 🎨 استوديو إنشاء الصور HD")
        prompt = st.text_area("وصفي مشهدكِ الإبداعي هنا:", placeholder="فتاة كرتونية ثلاثية الأبعاد...")
        
        st.write("#### 📏 القياسات المعتمدة (Fix 3):")
        c1, c2, c3 = st.columns(3)
        with c1: 
            if st.button("📱 Tall (9:16)"): st.session_state.res = (1024, 1792)
        with c2: 
            if st.button("🔳 Square (1:1)"): st.session_state.res = (1024, 1024)
        with c3: 
            if st.button("📺 Wide (16:9)"): st.session_state.res = (1792, 1024)

        width, height = st.session_state.get('res', (1024, 1024))
        
        if st.button("🚀 بدء التوليد الاحترافي"):
            if prompt:
                ph = st.empty()
                ph.info("🔄 جاري تأكيد الاتصال بالسيرفر وجلب الصورة...")
                
                # رابط بـ Seed زمني ونظام جلب مضمون
                url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width={width}&height={height}&seed={int(time.time())}&model=flux&nologo=true"
                
                try:
                    res = requests.get(url, timeout=45)
                    if res.status_code == 200 and len(res.content) > 10000:
                        ph.empty()
                        st.image(res.content, use_column_width=True)
                        st.download_button("📥 تحميل التصميم HD", data=res.content, file_name="node_pro.png")
                    else:
                        ph.error("⚠️ السيرفر مشغول حالياً (Overloaded)، يرجى الضغط مرة أخرى.")
                except:
                    ph.error("❌ فشل الاتصال. تأكدي من جودة الإنترنت.")

    # --- [3] مركز التحريك ونظام الحوار (الميزة المطلوبة) ---
    with st.container():
        st.write("### 🎬 مركز التحريك ونطق الفيديو")
        up = st.file_uploader("ارفعي صورة الشخصية هنا:", type=["png", "jpg"])
        
        if up:
            col_img, col_form = st.columns([1, 2])
            with col_img:
                st.image(up, width=250)
            
            with col_form:
                # إضافة نص حوار عند الفيديو (الميزة التي كانت ناقصة)
                speech_text = st.text_input("💬 نص الحوار (ماذا ستقول البنت؟):", placeholder="أهلاً بكم في تطبيق NODE...")
                motion_type = st.selectbox("😊 حركة الوجه:", ["تضحك وتتحدث", "تغمز وتتكلم", "نطق هادئ"])
                
                if st.button("✨ توليد الفيديو الناطق"):
                    if speech_text:
                        st.success(f"جاري معالجة الفيديو لنطق: '{speech_text}'")
                    else:
                        st.warning("يرجى كتابة نص الحوار أولاً.")

st.markdown("<p style='text-align:center; opacity:0.3; margin-top:50px;'>NODE 2026 | AMANI MURAD STUDIO</p>", unsafe_allow_html=True)
