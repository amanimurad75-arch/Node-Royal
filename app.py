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
if 'is_auth' not in st.session_state: st.session_state.is_auth = False

col_title, col_auth = st.columns([3, 1])
with col_title:
    st.markdown("<div class='node-header'>NODE</div>", unsafe_allow_html=True)
with col_auth:
    if not st.session_state.is_auth:
        if st.button("👤 دخول Google"):
            st.session_state.is_auth = True; st.rerun()
    else:
        st.markdown(f'<div class="auth-box">👤 <b>أماني مراد</b><br><small>amani.murad.75@gmail.com</small></div>', unsafe_allow_html=True)
        if st.button("خروج"):
            st.session_state.is_auth = False; st.rerun()

if st.session_state.is_auth:
    # --- [الكتلة 3]: استوديو الصور (نظام القياسات Fix 3 + حل مشكلة العرض) ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.subheader("🎨 استوديو إنشاء الصور HD")
    prompt = st.text_area("وصفي مشهدكِ الإبداعي:", placeholder="فتاة بأسلوب بيكسار تضحك...")

    st.write("#### 📏 القياسات المعتمدة (Fix 3):")
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("📱 9:16 (Tall)"): st.session_state.dims = (1024, 1792)
    with c2: 
        if st.button("🔳 1:1 (Square)"): st.session_state.dims = (1024, 1024)
    with c3: 
        if st.button("📺 16:9 (Wide)"): st.session_state.dims = (1792, 1024)

    width, height = st.session_state.get('dims', (1024, 1024))
    
    if st.button("🚀 بدء التوليد"):
        if prompt:
            placeholder = st.empty()
            placeholder.info("⏳ NODE يتواصل مع السيرفر.. يرجى الانتظار لنقوم بسحب الصورة HD")
            
            # رابط بـ Seed زمني فريد لضمان صورة جديدة دائماً
            url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width={width}&height={height}&seed={int(time.time())}&model=flux"
            
            # --- حل مشكلة عرض الصورة (بطلنا جحشنة!) ---
            image_data = None
            for attempt in range(3): # محاولة الجلب 3 مرات للتأكد من السيرفر
                try:
                    res = requests.get(url, timeout=45)
                    if res.status_code == 200 and len(res.content) > 10000: # التأكد أن الملف صورة حقيقية وليس فارغاً
                        image_data = res.content
                        break
                    time.sleep(2) # انتظار قليل بين المحاولات
                except:
                    continue

            if image_data:
                placeholder.empty()
                st.image(image_data, use_column_width=True)
                st.download_button("📥 حفظ الصورة", data=image_data, file_name="node_pro.png")
            else:
                placeholder.error("❌ السيرفر مشغول جداً. يرجى الضغط على 'بدء التوليد' مرة أخرى.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- [الكتلة 4]: مركز التحريك والنطق (ثابت) ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.subheader("🎬 مركز التحريك والنطق العربي")
    up_img = st.file_uploader("ارفعي صورة الشخصية هنا:", type=["png", "jpg"])
    
    if up_img:
        st.image(up_img, width=250)
        voice_input = st.text_input("💬 النص العربي الذي ستنطقه الفتاة:")
        motion_choice = st.selectbox("😊 اختر تعبير الوجه:", ["تضحك وتتحدث", "تغمز وتتكلم", "نطق هادئ"])
        
        if st.button("✨ إنتاج فيديو ناطق"):
            if voice_input:
                st.success(f"جاري تحضير فيديو ينطق: '{voice_input}' بحركة: {motion_choice}")
            else:
                st.warning("يرجى كتابة نص النطق أولاً.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align:center; opacity:0.3;'>إشراف وتطوير: أماني مراد | NODE 2026</p>", unsafe_allow_html=True)
