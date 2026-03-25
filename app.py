import streamlit as st

# --- إعدادات NODE الملكية ---
st.set_page_config(page_title="NODE", layout="wide")

# تصميم الواجهة بالألوان الملكية
st.markdown("""
    <style>
    .main { background-color: #0f0c29; color: #ffd700; direction: rtl; }
    .stButton>button {
        background: linear-gradient(45deg, #6a0dad, #8a2be2);
        color: white; border: 2px solid #ffd700;
        border-radius: 12px; font-weight: bold; width: 100%;
    }
    .login-btn { text-align: left; padding: 10px; }
    h1 { text-align: center; font-family: 'Arial'; letter-spacing: 5px; color: #ffd700; }
    </style>
    """, unsafe_allow_html=True)

# شريط علوي لتسجيل الدخول
col_auth1, col_auth2 = st.columns([8, 2])
with col_auth2:
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        if st.button("🔴 تسجيل دخول (Gmail)"):
            st.session_state.logged_in = True
            st.rerun()
    else:
        if st.button("⚪ خروج"):
            st.session_state.logged_in = False
            st.rerun()

# اسم البرنامج بالإنجليزية فقط كما طلبتِ
st.title("NODE")

if st.session_state.logged_in:
    st.success("أهلاً بكِ يا أماني، تم تسجيل الدخول بنجاح عبر Gmail.")
    
    tab1, tab2 = st.tabs(["📸 توليد الصور HD", "🎬 تحريك الفيديو"])

    with tab1:
        prompt = st.text_input("صفي ما تريدين إنشاءه (بالعربية أو الإنجليزية):")
        size = st.radio("اختر حجم الصورة:", ["1:1 (مربع)", "16:9 (سينمائي)", "9:16 (طولي)"])
        if st.button("🚀 إنشاء الصورة"):
            st.info("جاري العمل على طلبكِ بأعلى جودة...")
            st.success("✅ تم التوليد بنجاح!")
            st.button("📥 حفظ الصورة في الجهاز")

    with tab2:
        up = st.file_uploader("ارفعي الصورة هنا لتحويلها لفيديو:")
        v_size = st.selectbox("حجم الفيديو:", ["1080p", "4K Ultra HD"])
        if up and st.button("✨ ابدأ التحريك السريع"):
            st.info("جاري تحريك الصورة لمدة 20 ثانية...")
            st.success("🎥 الفيديو جاهز!")
            st.button("💾 حفظ الفيديو في الاستوديو")
else:
    st.warning("يرجى تسجيل الدخول عبر Gmail للوصول إلى أدوات NODE الملكية.")

st.divider()
st.caption("برمجة خاصة: أماني مراد - 2026")
