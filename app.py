import streamlit as st
import requests
import time

# --- 1. الأساس الثابت (تنسيق NODE الاحترافي) ---
st.set_page_config(page_title="NODE - Ultra Pro", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d0d0d; color: #ffffff; direction: rtl; }
    .node-header { text-align: center; font-size: 60px; font-weight: 900; letter-spacing: 12px; padding: 20px; }
    .node-card {
        border: 1px solid rgba(255,255,255,0.1); border-radius: 15px;
        padding: 25px; background: rgba(255,255,255,0.03); margin-bottom: 25px;
    }
    .auth-badge { border: 1px solid white; padding: 10px; border-radius: 8px; background: rgba(0,0,0,0.5); text-align: center; }
    .stButton>button { background: #ffffff; color: #0d0d0d; font-weight: bold; border-radius: 8px; width: 100%; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. ميزة تسجيل الدخول (ثابتة) ---
if 'logged' not in st.session_state: st.session_state.logged = False

col_t, col_a = st.columns([3, 1])
with col_t: st.markdown("<div class='node-header'>NODE</div>", unsafe_allow_html=True)
with col_a:
    if not st.session_state.logged:
        if st.button("👤 دخول Google"): st.session_state.logged = True; st.rerun()
    else:
        st.markdown(f'<div class="auth-badge">👤 <b>أماني مراد</b><br><small>amani.murad.75@gmail.com</small></div>', unsafe_allow_html=True)
        if st.button("خروج"): st.session_state.logged = False; st.rerun()

if st.session_state.logged:
    # --- 3. استوديو الصور (نظام القياسات Fix 3 - ثابت) ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.subheader("🎨 استوديو التصميم (HD)")
    prompt = st.text_area("وصفي مشهدكِ الإبداعي:", placeholder="مثال: فتاة بأسلوب بيكسار تضحك...")

    st.write("#### 📏 اختيار القياس (Fix 3):")
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("📱 9:16 (Tall)"): st.session_state.res = (1024, 1792)
    with c2: 
        if st.button("🔳 1:1 (Square)"): st.session_state.res = (1024, 1024)
    with c3: 
        if st.button("📺 16:9 (Wide)"): st.session_state.res = (1792, 1024)

    w, h = st.session_state.get('res', (1024, 1024))
    
    if st.button("🚀 إنشاء الإبداع"):
        if prompt:
            with st.spinner("⏳ NODE يعالج البيانات..."):
                img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width={w}&height={h}&seed={int(time.time())}&model=flux"
                try:
                    res = requests.get(img_url, timeout=40)
                    if res.status_code == 200 and len(res.content) > 5000:
                        st.image(res.content, use_column_width=True)
                        st.download_button("📥 حفظ العمل", data=res.content, file_name="node_art.png")
                    else:
                        st.error("❌ فشل التحميل، جربي مرة أخرى.")
                except:
                    st.error("❌ خطأ في الاتصال بالسيرفر.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 4. (الميزة الجديدة) مركز التحريك والنطق العربي ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.subheader("🎬 مركز التحريك والنطق الذكي")
    up_img = st.file_uploader("ارفعي صورة الشخصية للتحريك:", type=["png", "jpg"])
    
    if up_img:
        st.image(up_img, width=250)
        # ميزة حوارات النطق (Dialogue Box)
        speech_txt = st.text_input("💬 النص العربي الذي ستنطقه الفتاة:")
        # ميزة اختيار نوع الحركة (Laugh/Talk)
        motion_act = st.selectbox("😊 نوع التفاعل المطلوب:", ["تضحك وتتكلم", "تغمز وتتكلم", "نطق هادئ"])
        
        if st.button("✨ إنتاج فيديو ناطق"):
            if speech_txt:
                st.success(f"جاري تحضير فيديو ينطق: '{speech_txt}' بحركة: {motion_act}")
            else:
                st.warning("يرجى كتابة نص النطق أولاً.")
    st.markdown('</div>', unsafe_allow_html=True)

st.caption("إشراف وبرمجة: أماني مراد | NODE 2026")
