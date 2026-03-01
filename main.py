import streamlit as st
import re
import time

# ================= PAGE CONFIG ================= #
st.set_page_config(
    page_title="Smart Job Scam Detector",
    page_icon="🛡️",
    layout="centered"
)

# ================= CSS (PREMIUM UI) ================= #
st.markdown("""
<style>
body {
    background-color: #020617;
    color: #e5e7eb;
}
.block-container {
    padding-top: 2rem;
}
.glass {
    background: rgba(17, 25, 40, 0.75);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 28px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.55);
    margin-bottom: 25px;
}
.title {
    font-size: 2.5rem;
    font-weight: 800;
    text-align: center;
}
.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 30px;
}
.big-score {
    font-size: 60px;
    font-weight: 900;
    text-align: center;
}
.stButton > button {
    background: linear-gradient(135deg, #6366f1, #22d3ee);
    color: black;
    border-radius: 12px;
    padding: 0.8rem;
    font-weight: 700;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR ================= #
st.sidebar.title("🛡️ Job Scam Detector")
st.sidebar.write("Version 1.0")
st.sidebar.write("Built with Python & Streamlit")
st.sidebar.markdown("---")
st.sidebar.write("🔍 Paste job description")
st.sidebar.write("📊 Get risk score")
st.sidebar.write("⚠️ Avoid scams")

# ================= HEADER ================= #
st.markdown("<div class='title'>🛡️ Smart Job Scam Detector</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Real-time risk analysis of job descriptions</div>",
    unsafe_allow_html=True
)

# ================= DETECTION LOGIC ================= #
def detect(text):
    neg = []
    if re.search(r"urgent|immediate|apply now|limited", text, re.I):
        neg.append("Urgency language")
    if re.search(r"no interview", text, re.I):
        neg.append("No interview")
    if re.search(r"whatsapp|telegram|\+\d{10,}", text, re.I):
        neg.append("Unprofessional contact")
    if re.search(r"work from home|easy money|guaranteed", text, re.I):
        neg.append("Too good to be true")
    if re.search(r"fee|registration|training fee", text, re.I):
        neg.append("Fee requested")

    pos = []
    if re.search(r"company|pvt|ltd|llp|inc", text, re.I):
        pos.append("Company mentioned")
    if re.search(r"interview|technical round|hr round", text, re.I):
        pos.append("Interview process")
    if re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text):
        pos.append("Professional email")

    score = len(neg) * 20 - len(pos) * 10
    score = max(0, min(score, 100))

    return neg, pos, score

def highlight(text, words):
    for w in words:
        text = re.sub(
            w,
            f"<span style='color:#ef4444; font-weight:700'>{w}</span>",
            text,
            flags=re.I
        )
    return text

# ================= TABS ================= #
tab1, tab2 = st.tabs(["🔍 Analyze Job", "ℹ️ How It Works"])

# ================= TAB 1 ================= #
with tab1:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    job_text = st.text_area(
        "Paste Job Description",
        height=220,
        placeholder="Paste the complete job description here..."
    )
    analyze = st.button("🔍 Analyze Job", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if analyze:
        if len(job_text.strip()) < 30:
            st.warning("Please enter a longer job description.")
        else:
            with st.spinner("Analyzing job post..."):
                time.sleep(1)
                neg, pos, score = detect(job_text)

            st.markdown("<div class='glass'>", unsafe_allow_html=True)

            # BIG SCORE
            color = "#22c55e"
            label = "LIKELY REAL"
            if score >= 70:
                color = "#ef4444"
                label = "FAKE JOB"
            elif score >= 40:
                color = "#f59e0b"
                label = "SUSPICIOUS"

            st.markdown(
                f"<div class='big-score' style='color:{color}'>{score}%</div>",
                unsafe_allow_html=True
            )
            st.markdown(f"<h3 style='text-align:center'>{label}</h3>", unsafe_allow_html=True)
            st.progress(score / 100)

            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='glass'>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("🔴 Red Flags")
                if neg:
                    for n in neg:
                        st.write("•", n)
                else:
                    st.write("None")

            with col2:
                st.subheader("🟢 Positive Signals")
                if pos:
                    for p in pos:
                        st.write("•", p)
                else:
                    st.write("None")

            st.markdown("</div>", unsafe_allow_html=True)

            # Highlight text
            if neg:
                st.markdown("<div class='glass'>", unsafe_allow_html=True)
                st.subheader("📌 Highlighted Issues")
                st.markdown(
                    highlight(job_text, neg),
                    unsafe_allow_html=True
                )
                st.markdown("</div>", unsafe_allow_html=True)

# ================= TAB 2 ================= #
with tab2:
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.markdown("""
    ### How this works
    - Detects scam patterns using text rules  
    - Assigns a risk score (0–100)  
    - Highlights suspicious phrases  
    - Gives instant decision support  

    ⚠️ This is a risk-analysis tool, not absolute verification.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

st.caption("⚠️ Always verify jobs through official company websites.")