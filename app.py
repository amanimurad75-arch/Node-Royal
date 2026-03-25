import streamlit as st
import requests
from io import BytesIO

# --- إعدادات الواجهة الرسومية NODE الملكية ---
st.set_page_config(page_title="NODE - Royal Edition", layout="wide")

# التصميم بالأبيض الثلجي والأرجواني الملكي للواجهة بأكملها
st.markdown("""
    <style>
    /* خلفية التطبيق أرجوانية ملكية عميقة */
    .stApp { background-color: #2d0050; color: #f0f8ff; direction: rtl; }
    
    /* عنوان NODE بالأبيض الثلجي اللامع */
    .hero-title {
        text-align: center; font-size: 55px; font-weight: bold;
        color: #f0f8ff; text-shadow: 0px 0px 15px rgba(255,255,255,0.7);
        padding: 10px; margin-bottom: 5px;
    }

    /* البوكسات الاحترافية بإطار ثلجي (grok-style panels) */
    .animated-box-outer {
        border: 2px solid #f0f8ff; /* إطار أبيض ثلجي */
        border-radius: 20px;
        padding: 5px; /* مسافة بين الإطار والمربع الداخلي */
        margin-top: 15px;
        backdrop-filter: blur(5px);
    }
    .animated-box-inner {
        background-color: rgba(106, 13, 173, 0.5); /* أرجواني مختلف (شفاف) */
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        color: white;
    }
    
    /* أيقونة الصورة الكبيرة داخل البوكس */
    .image-icon { font-size: 60px; color: #ffd700; margin-bottom: 10px; cursor: pointer; }
    
    /* أيقونة الزائد (+) الذهبيه */
    .plus-icon { font-size: 30px; color: #ffd700; font-weight: bold; margin-left: 5px; }

    .stButton>button {
        background: linear-gradient(45deg, #f0f8ff, #e0e0e0);
        color: #2d0050; font-weight: bold; border-radius: 10px; width: 100%; height: 3em;
    }
    
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        border: 1px solid white; border-radius: 10px; color: white; background: rgba(255,255,255,0.1);
    }
    .user-info { border: 2px solid white; border-radius: 10px; padding: 10px; background: #4b0082; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# نظام الدخول
if 'auth' not in st.session_state: st.session_state.auth = False

col_h1, col_h2 = st.columns([7, 3])
with col_h2:
    if st.session_state.auth:
        st.markdown(f'<div class="user-info">👤 <b>أماني مراد</b><br><small>amani.murad.75@gmail.com</small></div>', unsafe_allow_html=True)
    else:
        if st.button("🔴 دخول عبر Gmail"): st.session_state.auth = True; st.rerun()

# العنوان الملكي
st.markdown("<div class='hero-title'>NODE</div>", unsafe_allow_html=True)

if st.session_state.auth:
    # --- صفحة واحدة مدمجة ---
    st.markdown("<h3>📸 إنشاء صورة ثلجية HD</h3>", unsafe_allow_html=True)
    prompt = st.text_input("صفي إبداعكِ القادم الملكي (بالعربية أو الإنجليزية):", placeholder="مثال: رائد فضاء في غابة أرجوانية...")
    
    col_a1, col_a2 = st.columns([8, 2])
    with col_a2:
        generate_btn = st.button("🚀 إنشاء")
        
    if generate_btn and prompt:
        with st.spinner("جاري استحضار الصورة من السيرفر..."):
            img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed=5"
            
            try:
                response = requests.get(img_url)
                if response.status_code == 200:
                    # عرض الصورة كـ "وجة رسومية" متكاملة
                    st.markdown('<div class="animated-box-outer">', unsafe_allow_html=True)
                    st.image(img_url, use_column_width=True, caption="إبداع NODE")
                    
                    # بوكس البيانات السفلي للصورة
                    st.markdown(f"""
                        <div class="animated-box-inner">
                            <span class="plus-icon">+</span>
                            <p style="margin:0;"><b>القياس:</b> 1024x1024 HD</p>
                            <p style="margin:0;"><b>الحالة:</b> صورة رقمية جاهزة</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.download_button("📥 حفظ الصورة", data=response.content, file_name="node.png", mime="image/png")
                else:
                    st.error("عذراً، واجهنا مشكلة في جلب الصورة. تأكدي من الاتصال.")
            except Exception as e:
                st.error(f"خطأ في النظام: {e}")

    st.divider()

    # --- بوكس التحريك السفلي (طلب أماني الجديد) ---
    st.markdown("<h3>🎬 مركز تحريك الصور</h3>", unsafe_allow_html=True)
    
    # الإطار الأبيض والداخلي الأرجواني
    with st.container():
        st.markdown("""
            <div class="animated-box-outer">
                <div class="animated-box-inner">
                    <div class="image-icon">🖼️</div>
                    <p style="margin:0;"><b>ارفعي صورتكِ للتحريك الملكي</b></p>
                    <small>التحويل إلى فيديو احترافي</small>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # الزر الذي يفتح الملفات
        up_file = st.file_uploader("", type=["png", "jpg", "jpeg"], key="up_animation")
        
        if up_file:
            st.image(up_file, caption="الصورة التي رفعتِها", width=300)
            
            col_b1, col_b2, col_b3 = st.columns(3)
            with col_b1: size = st.selectbox("القياس:", ["9:16", "16:9", "1:1"])
            with col_b2: duration = st.selectbox("المدة:", ["5 ثوانٍ", "10 ثوانٍ", "20 ثانية"])
            with col_b3: type_out = st.selectbox("النوع:", ["صورة فقط", "فيديو كامل الشاشة"])
            
            if st.button("✨ ابدأ التحويل الملكي"):
                st.info("جاري المعالجة... سيظهر الفيديو هنا")
                # بوكس بيانات التحريك
                st.markdown(f"""
                    <div class="animated-box-outer">
                        <div class="animated-box-inner">
                            <span class="plus-icon">+</span>
                            <p style="margin:0;"><b>المدة:</b> {duration}</p>
                            <p style="margin:0;"><b>القياس المختار:</b> {size}</p>
                            <p style="margin:0;"><b>النوع:</b> {type_out}</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

else:
    st.markdown("<h3 style='text-align:center; color: white;'>يرجى تسجيل الدخول للوصول إلى NODE.</h3>", unsafe_allow_html=True)

st.caption("برمجة وتطوير: أماني مراد | NODE 2026")
