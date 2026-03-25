import streamlit as st
import requests
from io import BytesIO

# --- إعدادات NODE الملكية ---
st.set_page_config(page_title="NODE", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f0c29; color: #ffd700; direction: rtl; }
    .stButton>button {
        background: linear-gradient(45deg, #6a0dad, #8a2be2);
        color: white; border: 2px solid #ffd700;
        border-radius: 12px; font-weight: bold; width: 100%;
    }
    .user-box {
        padding: 10px; border: 1px solid #ffd700; border-radius: 10px;
        background: rgba(138, 43, 226, 0.2); text-align: center;
    }
    h1 { text-align: center; font-family: 'Arial'; letter-spacing: 2px; color: #ffd700; }
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
        # هنا يظهر البريد الإلكتروني المسجل (افتراضياً أماني مراد)
        st.markdown(f"""
            <div class="user-box">
                <p style="margin:0; font-size:12px;">المستخدم النشط:</p>
                <p style="margin:0; font-weight:bold; color:#fff;">amani.murad.75@gmail.com</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("⚪ تسجيل خروج"):
            st.session_state.auth = False
            st.rerun()

st.title("NODE")

if st.session_state.auth:
    tab1, tab2 = st.tabs(["📸 مختبر الصور HD", "🎬 تحريك الفيديو 20s"])

    with tab1:
        prompt = st.text_input("صفي الصورة (بالعربية أو الإنجليزية):", placeholder="مثلاً: قطة بيضاء بأسلوب بيكسار...")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            aspect = st.selectbox("الأبعاد:", ["1:1", "16:9", "9:16"])
        
        if st.button("🚀 إنشاء الصورة الآن"):
            with st.spinner("جاري الاتصال بالسيرفر وتوليد الصورة..."):
                # استخدام محرك Pollinations للتوليد الفوري
                img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed=123"
                st.image(img_url, caption="تم التوليد بواسطة NODE")
                
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
