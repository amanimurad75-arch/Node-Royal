import streamlit as st
import time

# --- إعدادات Node الملكي ---
st.set_page_config(page_title="Node Royal", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f0c29; color: #ffd700; }
    .stButton>button {
        background: linear-gradient(45deg, #6a0dad, #8a2be2);
        color: white; border: 2px solid #ffd700;
        border-radius: 15px; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 مجمع Node الملكي للمنشئين")

tab1, tab2 = st.tabs(["📸 توليد الصور", "🎬 تحريك الفيديو (20 ثانية)"])

with tab1:
    prompt = st.text_input("وصف الصورة:")
    if st.button("🚀 إنشاء بدون اختناق"):
        with st.spinner("جاري التوريد..."):
            time.sleep(3)
            st.success("✅ تم التوليد بنجاح وبدون علامة مائية!")

with tab2:
    st.info("💡 ميزة المنشئين: فيديو مدته 20 ثانية حصرياً لـ Node.")
    up = st.file_uploader("ارفع صورتك هنا")
    if up and st.button("✨ ابدأ التحريك"):
        st.video("https://www.w3schools.com/html/mov_bbb.mp4")
