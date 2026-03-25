import streamlit as st
import requests
from io import BytesIO

# --- إعدادات NODE الملكية المتطورة ---
st.set_page_config(page_title="NODE", layout="wide")

st.markdown("""
    <style>
    /* خلفية التطبيق أرجوانية ملكية عميقة */
    .main { background-color: #2d0050; color: #f0f8ff; direction: rtl; }
    
    /* العنوان بالأبيض الثلجي */
    .hero-title {
        text-align: center; font-size: 55px; font-weight: bold;
        color: #f0f8ff; text-shadow: 0px 0px 15px rgba(255,255,255,0.5);
        padding: 20px;
    }

    /* بوكس معلومات المستخدم - تماماً مثل واجهة Imagine */
    .user-box {
        padding: 15px; border: 2px solid #ffd700; border-radius: 12px;
        background: rgba(138, 43, 226, 0.2); text-align: center;
        margin-bottom: 20px;
    }
    
    /* بوكس المعلومات السفلي - أرجواني مختلف */
    .footer-box {
        background-color: rgba(106, 13, 173, 0.4);
        border: 2px solid #f0f8ff; border-radius: 15px;
        padding: 15px; margin-top: 20px; text-align: center;
    }

    /* زر الزائد (+) الملكي */
    .plus-btn {
        font-size: 40px; color: #ffd700; font-weight: bold;
        margin-bottom: 5px; display: block;
    }

    .stButton>button {
        background: linear-gradient(45deg, #f0f8ff, #e0e0e0);
        color: #2d0050; border-radius: 10px; font-weight: bold; width: 100%; height: 3em;
    }
    
    .stSelectbox, .stTextInput { border: 1px solid white; border-radius: 8px; color: white; }
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة الدخول والمعلومات
if 'auth' not in st.session_state: st.session_state.auth = False

# شريط المعلومات العلوي
col_header1, col_header2 = st.columns([7, 3])

with col_header2:
    if not st.session_state.auth:
        if st.button("🔴 دخول عبر Gmail"):
            st.session_state.auth = True
            st.rerun()
    else:
        # هنا يظهر بوكس معلومات المستخدم (أماني مراد)
        st.markdown(f"""
            <div class="user-box">
                <img src="https://avatar.iran.liara.run/public" width="50" style="border-radius:50%; margin-bottom:10px;">
                <p style="margin:0; font-weight:bold; color:white; font-size:18px;">أماني مراد</p>
                <p style="margin:0; color:white;">amani.murad.75@gmail.com</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("⚪ تسجيل خروج"):
            st.session_state.auth = False
            st.rerun()

# العنوان الملكي الجديد
st.markdown("<div class='hero-title'>NODE</div>", unsafe_allow_html=True)

if st.session_state.auth:
    tab1, tab2 = st.tabs(["📸 مختبر الصور HD", "🎬 تحريك الفيديو (جميع القياسات)"])

    with tab1:
        st.info("قسم توليد الصور الملكي")
        prompt = st.text_input("صفي الصورة:")
        col_img1, col_img2 = st.columns(2)
        with col_img1:
            # أحجام الصور الحقيقية
            img_ratio = st.selectbox("حجم الصورة:", ["1:1 (مربع)", "16:9 (سينمائي)", "9:16 (طولي)"])
        with col_img2:
            img_quality = st.radio("الجودة:", ["HD", "Ultra HD", "4K"])
        
        if st.button("🚀 إنشاء وحفظ بالجهاز"):
            with st.spinner("جاري التوليد بأعلى جودة..."):
                # محرك التوليد الفوري
                img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed=42"
                st.image(img_url, caption="إبداع NODE")
                
                # بوكس القياسات أسفل الصورة
                st.markdown(f"""
                    <div class="footer-box">
                        <span class="plus-btn">+</span>
                        <p style="margin:0;"><b>القياس المختار:</b> {img_ratio}</p>
                        <p style="margin:0;"><b>النوع:</b> صورة رقمية ثلجية</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # زر التحميل الحقيقي للجهاز
                img_data = requests.get(img_url).content
                st.download_button("📥 حفظ الصورة في الاستوديو", data=img_data, file_name="node_image.png", mime="image/png")

    with tab2:
        st.info("قسم تحريك الفيديو الاحترافي")
        up = st.file_uploader("ارفعي الصورة المطلوب تحريكها...")
        
        if up is not None:
            st.image(up, caption="الصورة الأصلية", width=300)
            
            st.markdown("<h3>⚙️ إعدادات التحريك والسوشيال ميديا</h3>", unsafe_allow_html=True)
            vid_ratio = st.selectbox("اختر قياس السوشيال ميديا:", [
                "YouTube/Facebook (16:9 - أفقي)",
                "TikTok/Reels/Snap (9:16 - عمودي)",
                "Instagram Feed (1:1 - مربع)",
                "Cinema HD (21:9 - سينمائي)"
            ])
            vid_quality = st.radio("جودة الفيديو:", ["1080p HD", "4K Ultra HD"])
            vid_duration = st.selectbox("المدة:", ["5 ثوانٍ", "10 ثوانٍ", "20 ثانية"])
            
            if st.button("✨ ابدأ التحريك الملكي"):
                st.info("جاري المعالجة...")
                
                # بوكس معلومات الفيديو
                st.markdown(f"""
                    <div class="footer-box">
                        <span class="plus-btn">+</span>
                        <p style="margin:0;"><b>مدة الفيديو:</b> {vid_duration}</p>
                        <p style="margin:0;"><b>القياس المختار:</b> {vid_ratio}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # زر حفظ الفيديو للجهاز (محاكاة)
                st.download_button("📥 حفظ الفيديو في الاستوديو", data="mp4_binary_content", file_name="node_video.mp4", mime="video/mp4")

else:
    st.markdown("<h3 style='text-align:center;'>يرجى تسجيل الدخول للوصول إلى NODE.</h3>", unsafe_allow_html=True)

st.divider()
st.caption("برمجة وتطوير: أماني مراد - NODE 2026")
                
                # زر التحميل الحقيقي للجهاز
                try:
                    img_data = requests.get(img_url).content
                    st.download_button("📥 حفظ الصورة في الاستوديو", data=img_data, file_name="node_royal_art.png", mime="image/png")
                except:
                    st.error("عذراً، حدث خطأ في محرك التحميل.")

    with tab2:
        st.info("قسم تحريك الفيديو الاحترافي")
        up = st.file_uploader("ارفعي الصورة المطلوب تحريكها:")
        if up and st.button("✨ بدء التحريك الملكي"):
            st.info("جاري المعالجة... سيظهر الفيديو هنا")
else:
    st.warning("يرجى تسجيل الدخول لعرض بيانات حسابك والبدء في الاستخدام.")

st.divider()
st.caption("جميع الحقوق محفوظة: أماني مراد - NODE 2026")
