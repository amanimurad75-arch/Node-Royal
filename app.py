import streamlit as st
import requests
import time

# --- [1] الهوية البصرية الملكية (الأرجواني الملكي + الأبيض الثلجي) ---
st.set_page_config(page_title="NODE - Ultra Professional", layout="wide")

st.markdown("""
    <style>
    /* خلفية أرجوانية ملكية سادة */
    .stApp { background-color: #4B0082; color: #FFFAFA; direction: rtl; }
    
    /* هيدر NODE الثلجي */
    .node-header {
        text-align: center; font-size: 80px; font-weight: 900;
        letter-spacing: 15px; color: #FFFAFA; 
        text-shadow: 3px 3px 15px rgba(0,0,0,0.4);
        padding: 40px 0;
    }
    
    /* صناديق العمل (Cards) بحدود ثلجية */
    .node-card {
        border: 2px solid #FFFAFA; border-radius: 20px;
        padding: 30px; background: rgba(255, 250, 250, 0.1);
        margin-bottom: 30px;
    }
    
    /* الأزرار الثلجية بالكتابة الأرجوانية */
    .stButton>button {
        background: #FFFAFA !important; color: #4B0082 !important;
        font-weight: 900; border-radius: 12px; border: none;
        height: 3.8em; width: 100%; transition: 0.4s ease;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 25px #FFFAFA; }

    /* ✅ حل مشكلة الخط الأسود المواطن داخل البوكس الأبيض */
    /* جعل الخط داخل stTextArea و stTextInput أسود بالكامل */
    .stTextArea textarea, .stTextInput input {
        background-color: #FFFFFF !important; /* خلفية بيضاء */
        color: #000000 !important; /* الخط أسود وواضح جداً */
        border: 2px solid #FFFAFA !important; 
        text-align: right; direction: rtl; font-size: 18px !important;
    }
    /* جعل الخط التوضيحي (Placeholder) أسود خفيف */
    .stTextArea textarea::placeholder, .stTextInput input::placeholder {
        color: rgba(0,0,0,0.6) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- [2] نظام تسجيل الدخول والخروج (ثابت) ---
if 'auth_active' not in st.session_state: st.session_state.auth_active = False

st.markdown("<div class='node-header'>NODE</div>", unsafe_allow_html=True)

# قسم تسجيل الدخول (ثابت في الأعلى)
col_sp_l, col_auth_box = st.columns([4, 1])
with col_auth_box:
    if not st.session_state.auth_active:
        if st.button("👤 دخول Google"): st.session_state.auth_active = True; st.rerun()
    else:
        st.markdown(f'<div style="border:2px solid #FFFAFA; padding:10px; border-radius:12px; text-align:center; color:#FFFAFA;">👑 <b>أماني مراد</b></div>', unsafe_allow_html=True)
        if st.button("تسجيل الخروج"): st.session_state.auth_active = False; st.rerun()

if st.session_state.auth_active:
    # --- [3] استوديو الصور (حل السيرفر + القياسات Fix 3) ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.write("### 🎨 استوديو التصميم المتكامل")
    
    # بوكس الوصف الأبيض بالكتابة السوداء
    prompt = st.text_area("وصفي مشهدكِ الإبداعي القادم:", placeholder="اكتبي الوصف (الخط سيظهر باللون الأسود)...")

    # ✅ رجعت القياسات الثلاثة (Fix 3) - ما طلبتي حذفها
    st.write("#### 📏 اختيار القياس (Fix 3):")
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("📱 Tall (9:16)"): st.session_state.size_dim = (1024, 1792)
    with c2: 
        if st.button("🔳 Square (1:1)"): st.session_state.size_dim = (1024, 1024)
    with c3: 
        if st.button("📺 Wide (16:9)"): st.session_state.size_dim = (1792, 1024)

    w, h = st.session_state.get('size_dim', (1024, 1024))
    
    # زر بدء التوليد
    if st.button("🚀 بدء التوليد وعرض الصورة HD"):
        if prompt:
            loading_status = st.empty()
            loading_status.info("⏳ جاري سحب الإبداع من السيرفر.. بطلنا جحشنة يا ملكة!")
            url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width={w}&height={h}&seed={int(time.time())}&model=flux"
            try:
                res = requests.get(url, timeout=50)
                if res.status_code == 200 and len(res.content) > 15000:
                    loading_status.empty()
                    st.image(res.content, use_column_width=True, caption=f"إبداع أماني مراد - قياس {w}x{h}")
                    st.download_button("📥 حفظ التصميم الماسي", data=res.content, file_name="node_art.png")
                else:
                    loading_status.error("❌ السيرفر مشغول، حاولي مرة ثانية يا أماني.")
            except:
                loading_status.error("❌ فشل الاتصال بالسيرفر.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- [4] مركز التحريك و (بوكس الحوار العربي + بوكس التحميل) ---
    st.markdown('<div class="node-card">', unsafe_allow_html=True)
    st.write("### 🎬 مركز التحريك ونطق الفيديو")
    
    # ✅ رجعت بوكس تحميل الصور في مركز التحريك
    uploaded_image = st.file_uploader("ارفعي صورة الشخصية هنا لتحريكها:", type=["png", "jpg"])
    
    if uploaded_image:
        st.image(uploaded_image, width=280, caption="الشخصية المرفوعة")
        
        # ميزة بوكس الحوار العربي الثابتة
        st.write("#### 💬 إعدادات الحوار والنطق:")
        # بوكس الحوار الأبيض بالكتابة السوداء
        amani_chat = st.text_area("اكتبي هنا النص العربي الذي ستنطقه الشخصية:", placeholder="مثال: أهلاً بكِ أماني في عالم NODE...")
        
        motion_style = st.selectbox("😊 تعبير الوجه:", ["تضحك وتتحدث", "تغمز وتتكلم", "نطق ملكي هادئ"])
        
        if st.button("✨ إنتاج فيديو ناطق"):
            if amani_chat:
                st.success(f"✅ تم اعتماد النص العربي للنطق: '{amani_chat}'")
            else:
                st.warning("⚠️ يرجى كتابة نص النطق العربي أولاً.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- [5] تذييل الصفحة الملكي (ثابت) ---
st.markdown("<p style='text-align:center; opacity:0.8; color:#FFFAFA;'>إشراف وتطوير الملكة: أماني مراد | NODE 2026</p>", unsafe_allow_html=True)
