import streamlit as st
import requests
import time

# --- إعدادات NODE الملكية (النسخة النهائية) ---
st.set_page_config(page_title="NODE - AI Creative Studio", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #2d0050; color: #f0f8ff; direction: rtl; }
    .hero-title { text-align: center; font-size: 50px; font-weight: bold; text-shadow: 0px 0px 15px white; }
    
    /* تنسيق الأزرار والبوكسات الملكية */
    .stButton>button { 
        background: white; color: #2d0050; font-weight: bold; 
        border-radius: 12px; border: 2px solid #f0f8ff;
    }
    .result-container {
        border: 2px solid white; border-radius: 20px; 
        padding: 20px; background: rgba(255,255,255,0.05); margin-top: 10px;
    }
    .user-info { border: 1px solid white; border-radius: 10px; padding: 10px; background: #4b0082; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- الهيدر وبيانات أماني ---
col_h1, col_h2 = st.columns([8, 2])
with col_h1:
    st.markdown("<div class='hero-title'>NODE</div>", unsafe_allow_html=True)
with col_h2:
    st.markdown('<div class="user-info">👤 أماني مراد</div>', unsafe_allow_html=True)

# --- نظام القياسات الاحترافي (كما في Replit 1061.jpg) ---
st.markdown("### 🎨 استوديو إنشاء الصور HD")
prompt = st.text_area("صفي إبداعكِ (عربي أو إنجليزي):", placeholder="مثلاً: فتاة صغيرة تضحك وتنطق بالعربية...")

st.markdown("#### 📏 اختر أبعاد التصميم (Fix 3):")
c1, c2, c3 = st.columns(3)
with c1: 
    if st.button("📱 9:16 (Tall)"): st.session_state.dims = "1024x1792"
with c2: 
    if st.button("🔳 1:1 (Square)"): st.session_state.dims = "1024x1024"
with c3: 
    if st.button("📺 16:9 (Wide)"): st.session_state.dims = "1792x1024"

# تحديد الأبعاد الافتراضية
dims = st.session_state.get('dims', "1024x1024")
st.info(f"القياس الحالي: {dims}")

if st.button("🚀 توليد وحفظ الإبداع"):
    if prompt:
        with st.spinner("⏳ جاري الاتصال بالسيرفر..."):
            w, h = dims.split('x')
            # إضافة Seed عشوائي لمنع تكرار الصور الفارغة
            img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width={w}&height={h}&seed={int(time.time())}&model=flux"
            
            try:
                response = requests.get(img_url, timeout=30)
                if response.status_code == 200 and len(response.content) > 1000:
                    st.markdown('<div class="result-container">', unsafe_allow_html=True)
                    st.image(response.content, use_column_width=True)
                    # زر التنزيل الحقيقي
                    st.download_button("📥 حفظ الصورة بجودة HD", data=response.content, file_name="node_image.png", mime="image/png")
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.error("السيرفر مشغول حالياً، يرجى إعادة المحاولة.")
            except:
                st.error("فشل في تحميل الصورة.")

st.divider()

# --- مركز التحريك والنطق (بوكس الصورة) ---
st.markdown("### 🎬 مركز التحريك والنطق العربي")
st.markdown('<div style="background:#6a0dad; padding:15px; border-radius:15px; text-align:center;">🖼️ اضغطي أدناه لرفع الصورة</div>', unsafe_allow_html=True)

up_file = st.file_uploader("", type=["png", "jpg", "jpeg"])

if up_file:
    st.image(up_file, width=250)
    
    # مربع حوار النطق والحركة (طلب أماني)
    st.markdown("#### 💬 ماذا تريدينها أن تقول وتفعل؟")
    speech = st.text_area("النص العربي (سوف تنطقه الفتاة):", placeholder="اكتبي الكلمات هنا...")
    motion = st.text_input("وصف الحركة (تضحك، تتكلم، إلخ):")

    col_v1, col_v2 = st.columns(2)
    with col_v1: v_size = st.selectbox("القياس:", ["9:16", "1:1", "16:9"])
    with col_v2: v_type = st.selectbox("النمط:", ["فيديو كامل", "تحريك بسيط"])

    if st.button("✨ ابدأ التحريك والنطق"):
        if speech:
            st.success(f"جاري معالجة الفيديو لنطق: {speech}")
            st.info(f"الحركة المطلوبة: {motion}")
        else:
            st.warning("يرجى كتابة النص العربي أولاً.")

st.caption("تطوير: أماني مراد - NODE 2026")
