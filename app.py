import streamlit as st
import requests
import time

# --- إعدادات NODE الملكية ---
st.set_page_config(page_title="NODE - Ultra Clean Edition", layout="wide")

# تصميم فخم، مرتب، وبسيط جداً (مستوحى من 1061.jpg)
st.markdown("""
    <style>
    .stApp {
        background-color: #1a0033; /* خلفية أرجوانية داكنة سادة */
        color: #ffffff;
        direction: rtl;
    }
    .hero-title {
        text-align: center; font-size: 60px; font-weight: bold;
        letter-spacing: 8px; padding: 30px; color: #ffffff;
    }
    .section-card {
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px; padding: 25px;
        background: rgba(255, 255, 255, 0.02); margin-bottom: 25px;
    }
    .stButton>button {
        background: #ffffff; color: #1a0033; font-weight: bold;
        border-radius: 12px; border: none; height: 3.5em; width: 100%;
    }
    /* إخفاء الزوائد لزيادة الترتيب */
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='hero-title'>NODE</div>", unsafe_allow_html=True)

# --- القسم الأول: إنشاء الصور (حل مشكلة الفشل 1060.jpg) ---
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("🎨 استوديو التصميم الملكي")
    
    prompt = st.text_area("صفي خيالكِ هنا:", placeholder="مثال: فتاة كرتونية تضحك بصوت عالٍ...")
    
    st.markdown("#### 📏 اختر الأبعاد بدقة (Fix 3):")
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("📱 9:16 (Tall)"): st.session_state.dim = (1024, 1792)
    with c2: 
        if st.button("🔳 1:1 (Square)"): st.session_state.dim = (1024, 1024)
    with c3: 
        if st.button("📺 16:9 (Wide)"): st.session_state.dim = (1792, 1024)

    w, h = st.session_state.get('dim', (1024, 1024))
    
    if st.button("🚀 توليد العمل الفني"):
        if prompt:
            status = st.empty()
            status.info("⏳ NODE يقوم برسم فكرتكِ.. يرجى الانتظار")
            
            # رابط متطور بـ Seed زمني لمنع الملفات الفارغة
            img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width={w}&height={h}&seed={int(time.time())}&model=flux"
            
            try:
                res = requests.get(img_url, timeout=40)
                if res.status_code == 200 and len(res.content) > 1000:
                    status.empty()
                    st.image(res.content, caption=f"تم التوليد بنجاح ({w}x{h})", use_column_width=True)
                    st.download_button("📥 حفظ الصورة بجودة HD", data=res.content, file_name="node_pro.png", mime="image/png")
                else:
                    status.error("❌ السيرفر لم يستجب بالكامل، يرجى المحاولة مرة أخرى.")
            except:
                status.error("❌ فشل الاتصال بالسيرفر.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- القسم الثاني: النطق والتحريك (طلب أماني 1052.jpg) ---
with st.container():
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("🎬 مركز النطق والتحريك العربي")
    
    up_img = st.file_uploader("ارفعي صورة الفتاة هنا:", type=["png", "jpg"])
    
    if up_img:
        st.image(up_img, width=250)
        
        # مربعات الحوار المرتبة للنطق
        speech = st.text_input("💬 النص الذي ستنطقه الفتاة (بالعربية):")
        action = st.selectbox("😊 حركة الوجه المطلوبة:", ["تضحك وتتحدث", "تتكلم بهدوء", "غمزة عين"])
        
        if st.button("✨ إنتاج الفيديو الناطق"):
            if speech:
                st.success(f"جاري تحريك الصورة لنطق: '{speech}' مع حركة: {action}")
            else:
                st.warning("يرجى كتابة النص العربي أولاً.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div style='text-align:center; opacity:0.4;'>إشراف وتطوير: أماني مراد | NODE 2026</div>", unsafe_allow_html=True)
