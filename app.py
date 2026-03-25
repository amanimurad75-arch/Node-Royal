import streamlit as st
import requests

# --- إعدادات NODE الملكية ---
st.set_page_config(page_title="NODE", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #1a0033;
        background-image: radial-gradient(circle at center, #2d0050 0%, #1a0033 100%);
        color: #f0f8ff;
        direction: rtl;
    }
    
    /* رفع العنوان للأعلى قليلاً */
    .header-container {
        text-align: center;
        padding-top: 5vh; /* تحكم في الارتفاع من هنا */
        margin-bottom: 20px;
    }

    .hero-title {
        font-size: 85px; 
        font-weight: bold;
        color: #f0f8ff; 
        text-shadow: 0px 0px 30px rgba(255,255,255,0.9);
        letter-spacing: 12px;
    }

    /* بوكس تسجيل الدخول الملكي */
    .login-card {
        background: rgba(45, 0, 80, 0.6);
        border: 2px solid #f0f8ff; 
        border-radius: 25px;
        padding: 30px; 
        margin: 0 auto; 
        max-width: 420px;
        text-align: center;
        backdrop-filter: blur(15px);
        box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
    }

    .stButton>button {
        background: linear-gradient(45deg, #f0f8ff, #e0e0e0);
        color: #1a0033; 
        font-weight: bold; 
        border-radius: 15px; 
        height: 3.8em; 
        width: 100%;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 15px rgba(255,255,255,0.4);
    }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# واجهة البداية
if not st.session_state.auth:
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.markdown("<div class='hero-title'>NODE</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='margin-bottom:25px;'>مرحباً بكِ في NODE 🗝️</h3>", unsafe_allow_html=True)
    
    # خيار تسجيل الدخول عبر جوجل
    if st.button("🔴 تسجيل الدخول عبر Google"):
        st.session_state.auth = True
        st.session_state.user = "أماني مراد"
        st.rerun()
    
    st.markdown("<p style='margin:15px 0;'>أو</p>", unsafe_allow_html=True)
    
    # خيار إنشاء حساب
    with st.expander("✨ إنشاء حساب جديد"):
        new_email = st.text_input("البريد الإلكتروني:")
        new_pass = st.text_input("كلمة المرور:", type="password")
        if st.button("تأكيد الإنشاء والدخول"):
            if new_email and new_pass:
                st.session_state.auth = True
                st.session_state.user = new_email
                st.rerun()
            else:
                st.error("يرجى إدخال البيانات")
                
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # واجهة التطبيق المدمجة بعد الدخول
    st.markdown("<div style='text-align:center;'><h1 class='hero-title' style='font-size:40px;'>NODE</h1></div>", unsafe_allow_html=True)
    
    col_u, col_l = st.columns([8, 2])
    with col_u: st.write(f"🟢 المتصل الآن: **{st.session_state.user}**")
    with col_l: 
        if st.button("🚪 خروج"):
            st.session_state.auth = False
            st.rerun()

    st.divider()
    
    # القسم العملي (الصور والتحريك)
    st.markdown("<h3>📸 مختبر الصور HD</h3>", unsafe_allow_html=True)
    p = st.text_input("صفي إبداعكِ القادم:")
    if st.button("🚀 إنشاء الآن"):
        st.image(f"https://pollinations.ai/p/{p.replace(' ', '%20')}?width=1024&height=1024", use_column_width=True)

    st.divider()
    st.markdown("<h3>🎬 مركز التحريك الملكي</h3>", unsafe_allow_html=True)
    st.file_uploader("ارفعي الصورة هنا للتحريك:", type=["png", "jpg", "jpeg"])

st.caption("برمجة وتطوير: أماني مراد - NODE 2026")
