import streamlit as st
import requests
import time

# --- إعدادات النسخة العصرية جداً ---
st.set_page_config(page_title="NODE - Ultra Modern", layout="centered")

st.markdown("""
    <style>
    /* خلفية سوداء عميقة فخمة */
    .stApp { background-color: #000000; color: #e0e0e0; direction: rtl; }
    
    /* عنوان NODE بتأثير نيون خفيف */
    .node-header {
        text-align: center; font-size: 60px; font-weight: 800;
        letter-spacing: 12px; color: #ffffff; padding: 40px 0;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
    }
    
    /* أزرار القياسات (ستايل زجاجي Frosted Glass) */
    .stButton>button {
        background: rgba(255, 255, 255, 0.1); color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 5px; height: 3em; transition: 0.4s;
    }
    .stButton>button:hover {
        background: #ffffff; color: #000000; border: none;
    }
    
    /* مداخل النصوص */
    .stTextArea textarea { background-color: #111111; color: white; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='node-header'>NODE</div>", unsafe_allow_html=True)

# --- محرك الإنشاء الفائق ---
st.write("### ⚡ استوديو التصميم")
user_input = st.text_area("أدخلي وصفكِ الإبداعي هنا:", placeholder="مثلاً: فتاة بأسلوب بيكسار...")

# نظام القياسات المعتمد (Fix 3)
col_a, col_b, col_c = st.columns(3)
with col_a: 
    if st.button("TALL 9:16"): st.session_state.res = (1024, 1792)
with col_b: 
    if st.button("SQUARE 1:1"): st.session_state.res = (1024, 1024)
with col_c: 
    if st.button("WIDE 16:9"): st.session_state.res = (1792, 1024)

width, height = st.session_state.get('res', (1024, 1024))

if st.button("🚀 بـدء الـتـولـيـد"):
    if user_input:
        placeholder = st.empty()
        placeholder.markdown("🔍 **NODE يتواصل مع السيرفر.. يرجى الانتظار**")
        
        # رابط احترافي مع Seed فريد لكل طلب
        img_url = f"https://pollinations.ai/p/{user_input.replace(' ', '%20')}?width={width}&height={height}&seed={int(time.time())}&nologo=true"
        
        try:
            # محاولة جلب الصورة مع فحص الاستجابة (Fix لخطأ 1063)
            response = requests.get(img_url, timeout=40)
            if response.status_code == 200 and len(response.content) > 5000:
                placeholder.empty()
                st.image(response.content, use_column_width=True)
                st.download_button("📥 تحميل التصميم بجودة عالية", data=response.content, file_name="node_pro.png")
            else:
                placeholder.error("⚠️ السيرفر مشغول حالياً، يرجى إعادة المحاولة بعد ثوانٍ.")
        except:
            placeholder.error("❌ تعذر الاتصال بالسيرفر، تأكدي من الإنترنت.")

st.divider()

# --- مركز التحريك والنطق (التصميم العصرى) ---
st.write("### 🎬 مركز التحريك الذكي")
uploaded = st.file_uploader("ارفعي صورة الفتاة هنا:", type=['png', 'jpg'])

if uploaded:
    st.image(uploaded, width=280)
    speech_input = st.text_input("💬 النص العربي المنطوق (Voice-over):")
    
    if st.button("✨ مـعـالـجـة الـفـيـديـو"):
        if speech_input:
            st.info(f"جاري دمج الصوت العربي: {speech_input}")
        else:
            st.warning("يرجى إدخال النص أولاً.")

st.markdown("<br><p style='text-align:center; opacity:0.3;'>NODE 2026 | AMANI MURAD</p>", unsafe_allow_html=True)
