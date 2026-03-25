import streamlit as st
import requests
from io import BytesIO

# --- إعدادات NODE الملكية الفخمة ---
st.set_page_config(page_title="NODE", layout="wide")

st.markdown("""
    <style>
    /* الشاشة كاملة باللون الأرجواني الملكي */
    .main { background-color: #2d0050; color: #f0f8ff; direction: rtl; }
    
    /* عنوان NODE بالأبيض الثلجي */
    .hero-title {
        text-align: center; font-size: 60px; font-weight: bold;
        color: #f0f8ff; text-shadow: 0px 0px 15px rgba(255,255,255,0.6);
        padding: 15px; margin-bottom: 5px;
    }

    /* المربعات السفلية (البوكسات) بإطار ثلجي */
    .node-box {
        border: 2px solid #f0f8ff; border-radius: 20px;
        padding: 10px; margin-top: 15px; background-color: rgba(106, 13, 173, 0.3);
    }
    
    .plus-icon { font-size: 35px; color: #ffd700; font-weight: bold; text-align: center; }

    /* تنسيق أزرار التابلت */
    .stButton>button {
        background: linear-gradient(45deg, #f0f8ff, #e0e0e0);
        color: #2d0050; font-weight: bold; border-radius: 12px; height: 3.5em;
    }
    
    .user-card { border: 1px solid white; border-radius: 12px; padding: 10px; background: #4b0082; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# إدارة تسجيل الدخول
if 'auth' not in st.session_state:
    st.session_state.auth = False

# منطقة الحساب (أعلى اليمين)
col_h1, col_h2 = st.columns([7, 3])
with col_h2:
    if st.session_state.auth:
        st.markdown('<div class="user-card">👤 <b>أماني مراد</b><br><small>amani.murad.75@gmail.com</small></div>', unsafe_allow_html=True)
        if st.button("🚪 خروج"):
            st.session_state.auth = False
            st.rerun()
    else:
        if st.button("🔴 دخول Gmail"):
            st.session_state.auth = True
            st.rerun()

st.markdown("<div class='hero-title'>NODE</div>", unsafe_allow_html=True)

if st.session_state.auth:
    # --- القسم الأول: توليد الصور ---
    st.markdown("<h3>📸 مختبر الصور الثلجي</h3>", unsafe_allow_html=True)
    prompt = st.text_input("صفي الصورة التي تتخيلينها:", placeholder="مثلاً: قصر في الغيوم بأسلوب ديزني...")
    
    if st.button("🚀 إنشاء وحفظ"):
        with st.spinner("جاري الإبداع..."):
            img_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed=99"
            st.image(img_url, use_column_width=True)
            
            # بوكس البيانات تحت الصورة
            st.markdown('<div class="node-box"><div class="plus-icon">+</div><p style="text-align:center;">القياس: 1024x1024 HD<br>الحالة: جاهزة للتحميل</p></div>', unsafe_allow_html=True)
            
            img_data = requests.get(img_url).content
            st.download_button("📥 تنزيل الصورة للجهاز", data=img_data, file_name="node_art.png")

    st.divider()

    # --- القسم الثاني: تحريك الفيديو ---
    st.markdown("<h3>🎬 مركز التحريك (بوكس الصورة)</h3>", unsafe_allow_html=True)
    st.markdown('<div class="node-box"><div style="font-size:50px; text-align:center;">🖼️</div><p style="text-align:center;">اضغطي أدناه لرفع الصورة</p></div>', unsafe_allow_html=True)
    
    up = st.file_uploader("", type=["png", "jpg", "jpeg"])
    if up:
        st.image(up, width=280)
        c1, c2, c3 = st.columns(3)
        with c1: sz = st.selectbox("القياس:", ["9:16", "16:9", "1:1"])
        with c2: dr = st.selectbox("المدة:", ["10s", "20s"])
        with c3: mode = st.selectbox("النمط:", ["فيديو كامل", "سينمائي"])
        
        if st.button("✨ ابدأ التحريك"):
            st.info("جاري التحويل... سيظهر الفيديو هنا")
            st.markdown(f'<div class="node-box"><div class="plus-icon">+</div><p style="text-align:center;">القياس المختار: {sz}<br>المدة: {dr}</p></div>', unsafe_allow_html=True)

else:
    st.info("مرحباً بكِ في NODE.. يرجى تسجيل الدخول للبدء")

st.caption("تطوير: أماني مراد - 2026")
