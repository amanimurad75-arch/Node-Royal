import streamlit as st
import requests

# --- إعدادات NODE الملكية ---
st.set_page_config(page_title="NODE", layout="wide")

# التصميم بالأبيض الثلجي والخلفية الأرجوانية الغامقة الثابتة
st.markdown("""
    <style>
    /* الخلفية الأرجوانية الاحترافية */
    .stApp {
        background-color: #1a0033;
        background-image: radial-gradient(circle at center, #2d0050 0%, #1a0033 100%);
        color: #f0f8ff;
        direction: rtl;
    }
    
    /* جعل كلمة NODE في وسط الشاشة تماماً */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 60vh; /* ترفع العنوان للمنتصف */
    }

    .hero-title {
        font-size: 80px; 
        font-weight: bold;
        color: #f0f8ff; /* الأبيض الثلجي */
        text-shadow: 0px 0px 25px rgba(255,255,255,0.9);
        text-align: center;
        letter-spacing: 10px;
        margin-bottom: 20px;
    }

    .node-box {
        background: rgba(45, 0, 80, 0.7);
        border: 2px solid #f0f8ff; 
        border-radius: 20px;
        padding: 25px; 
        margin: 0 auto; 
        max-width: 450px;
        text-align: center;
        backdrop-filter: blur(10px);
    }

    .stButton>button {
        background: linear-gradient(45deg, #f0f8ff, #e0e0e0);
        color: #1a0033; 
        font-weight: bold; 
        border-radius: 12px; 
        height: 3.5em; 
        width: 100%;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة حالة الدخول
if 'auth' not in st.session_state:
    st.session_state.auth = False

# الحاوية المركزية للعنوان والدخول
if not st.session_state.auth:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown("<div class='hero-title'>NODE</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='node-box'>", unsafe_allow_html=True)
    st.subheader("🔐 تسجيل الدخول")
    
    mode = st.radio("", ["عبر Gmail", "إيميل مخصص"], horizontal=True)
    
    if mode == "عبر Gmail":
        if st.button("🔴 دخول سريع"):
            st.session_state.auth = True
            st.session_state.user = "أماني مراد"
            st.rerun()
    else:
        st.text_input("البريد الإلكتروني:")
        st.text_input("كلمة المرور:", type="password")
        if st.button("✨ دخول"):
            st.session_state.auth = True
            st.session_state.user = "مستخدم NODE"
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # واجهة العمل بعد الدخول
    st.markdown("<div class='hero-title' style='font-size:40px;'>NODE</div>", unsafe_allow_html=True)
    
    col_user, col_logout = st.columns([8, 2])
    with col_user: st.write(f"👤 مرحباً: **{st.session_state.user}**")
    with col_logout: 
        if st.button("🚪 خروج"):
            st.session_state.auth = False
            st.rerun()

    st.divider()
    
    # قسم إنشاء الصور
    st.markdown("<h3>📸 مختبر الصور HD</h3>", unsafe_allow_html=True)
    prompt = st.text_input("صفي فكرتكِ هنا:")
    if st.button("🚀 إنشاء"):
        img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024"
        st.image(img_url, use_column_width=True)

    st.divider()

    # بوكس التحريك
    st.markdown("<h3>🎬 مركز التحريك</h3>", unsafe_allow_html=True)
    st.markdown('<div class="node-box" style="border-style: dashed;"><div style="font-size: 40px;">🖼️</div><p>ارفعي صورتكِ للتحريك</p></div>', unsafe_allow_html=True)
    st.file_uploader("", type=["png", "jpg", "jpeg"])

st.caption("تطوير: أماني مراد - NODE 2026")
