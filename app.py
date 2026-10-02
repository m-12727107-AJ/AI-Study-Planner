from pathlib import Path

import streamlit as st
from study_buddy import show_study_buddy

# ==============================
# CONFIG
# ==============================
st.set_page_config(
    page_title="AI Study Planner",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================
# SESSION STATE
# ==============================
if "started" not in st.session_state:
    st.session_state.started = False
    
if "page" not in st.session_state:
    st.session_state.page = "Home"
    
if "coins" not in st.session_state:
    st.session_state.coins = 0

if "badges" not in st.session_state:
    st.session_state.badges = 0

if "study_minutes" not in st.session_state:
    st.session_state.study_minutes = 0

if "level" not in st.session_state:
    st.session_state.level = 1

if "xp" not in st.session_state:
    st.session_state.xp = 0
    
# ==============================
# SURFACE STYLE
# ==============================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff8d6 0%, #ffffff 55%, #eef3ff 100%);
}

.main-title {
    font-size: 48px;
    font-weight: 800;
    color: #172554;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 20px;
    color: #475569;
    text-align: center;
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 24px;
    border-radius: 22px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 25px rgba(15, 23, 42, 0.08);
    margin-bottom: 18px;
}

.card-title {
    font-size: 23px;
    font-weight: 700;
    color: #172554;
}

.card-text {
    color: #64748b;
    font-size: 16px;
}

.stButton > button {
    width: 100%;
    border-radius: 14px;
    min-height: 50px;
    font-weight: 700;
    border: none;
}
</style>
""", unsafe_allow_html=True)
# ==============================
# LOGO
# ==============================
logo_path = Path(__file__).parent / "logo_ai_study_planner.png"
if logo_path.exists():
    st.image(str(logo_path), width=180)




# ==============================
# SPLASH SCREEN
# ==============================
if not st.session_state.started:

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="main-title">📚 AI Study Planner</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Belajar lebih teratur, lebih bijak dan lebih menyeronokkan.</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    try:
        st.image(
            "/content/logo_ai_study_planner.png",
            width=260
        )
    except:
        st.markdown(
            "<h1 style='text-align:center;'>🧠📚</h1>",
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button("🚀 MULA", use_container_width=True):
            st.session_state.started = True
            st.rerun()

    st.stop()

# ==============================
# HEADER
# ==============================
top1, top2 = st.columns([5, 1])

with top1:
    st.markdown(
        '<div class="main-title" style="text-align:left;font-size:32px;">📚 AI Study Planner</div>',
        unsafe_allow_html=True
    )

with top2:
    if st.button("⚙️"):
        st.session_state.page = "Settings"

# ==============================
# PROFILE
# ==============================
st.markdown("""
<div class="card">
    <h2>👋 Hai, Student!</h2>
    <p>Selamat datang kembali. Jom teruskan pembelajaran hari ini.</p>
</div>
""", unsafe_allow_html=True)

# ==============================
# STATS - DASHBOARD STYLE
# ==============================

st.markdown("### 📊 Ringkasan Pembelajaran")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.metric(
        label="🏆 Lencana",
        value=st.session_state.badges
    )

with s2:
    st.metric(
        label="⏱️ Masa Belajar",
        value=f"{st.session_state.study_minutes} min"
    )

with s3:
    st.metric(
        label="🪙 Coins",
        value=st.session_state.coins
    )

with s4:
    st.metric(
        label="⭐ Level",
        value=max(1, st.session_state.xp // 100 + 1)
    )
# ==============================
# MENU UTAMA
# ==============================

st.markdown("## 🌟 Menu Utama")

m1, m2, m3, m4 = st.columns(4)

with m1:
    if st.button("🏠 Home\nDashboard utama", key="menu_home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()

with m2:
    if st.button("📅 Study Planner\nRancang jadual belajar", key="menu_planner", use_container_width=True):
        st.session_state.page = "Planner"
        st.rerun()

with m3:
    if st.button("🤖 AI Study Buddy\nPembantu belajar AI", key="menu_buddy", use_container_width=True):
        st.session_state.page = "Buddy"
        st.rerun()

with m4:
    if st.button("📝 Quiz\nUji pengetahuan", key="menu_quiz", use_container_width=True):
        st.session_state.page = "Quiz"
        st.rerun()

m5, m6, m7, m8 = st.columns(4)

with m5:
    if st.button("🎯 Missions\nSelesaikan misi", key="menu_missions", use_container_width=True):
        st.session_state.page = "Missions"
        st.rerun()

with m6:
    if st.button("🧠 Learning Path\nLaluan pembelajaran", key="menu_learning", use_container_width=True):
        st.session_state.page = "Learning"
        st.rerun()

with m7:
    if st.button("🏆 Progress\nLihat kemajuan", key="menu_progress", use_container_width=True):
        st.session_state.page = "Progress"
        st.rerun()

with m8:
    if st.button("⚙️ Settings\nTetapan aplikasi", key="menu_settings", use_container_width=True):
        st.session_state.page = "Settings"
        st.rerun()
# ==============================
# PAGE CONTENT
# ==============================

page = st.session_state.page

if page == "Home":

    st.markdown("## 🏠 Dashboard")

    d1, d2 = st.columns(2)

    with d1:
        st.markdown("""
        <div class="dashboard-card">
            <div class="dashboard-title">📅 Hari Ini</div>
            <div class="dashboard-text">
                Belum ada jadual pembelajaran.<br><br>
                Gunakan <b>Study Planner</b> untuk bina jadual.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with d2:
        st.markdown("""
        <div class="dashboard-card">
            <div class="dashboard-title">🧠 Learning Path</div>
            <div class="dashboard-text">
                Teruskan pembelajaran kamu dan bina kemahiran
                sedikit demi sedikit.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="motivation-card">
        <div class="motivation-title">💡 Motivasi Hari Ini</div>
        <div class="motivation-text">
            “Sedikit demi sedikit, lama-lama menjadi hebat!”
        </div>
    </div>
    """, unsafe_allow_html=True)


elif page == "Planner":

    st.markdown("## 📅 Study Planner")

    st.info("📚 Bahagian Study Planner akan digunakan untuk membina jadual ulang kaji.")


elif page == "Buddy":

    st.markdown("## 🤖 AI Study Buddy")

    show_study_buddy()


elif page == "Quiz":

    st.markdown("## 📝 Quiz")

    st.info("📝 Bahagian Quiz akan digunakan untuk menguji pengetahuan kamu.")


elif page == "Missions":

    st.markdown("## 🎯 Missions")

    st.info("🎯 Selesaikan misi untuk mendapatkan XP dan coins.")


elif page == "Learning":

    st.markdown("## 🧠 Learning Path")

    st.info("🧠 Ikuti laluan pembelajaran kamu di sini.")


elif page == "Progress":

    st.markdown("## 🏆 Progress")

    st.info("🏆 Pantau XP, level, coins dan lencana kamu di sini.")


elif page == "Settings":

    st.markdown("## ⚙️ Settings")

    st.info("⚙️ Tetapan aplikasi akan berada di sini.")

# ==============================
# FOOTER
# ==============================
st.markdown("---")

st.caption(
    "📚 AI Study Planner • Belajar dengan lebih bijak 🚀"
)
