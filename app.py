import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from ml_model import predict_pesticide_usage
from ai_model import generate_farm_ai_response, farm_chatbot_response

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="AI Farm Management Assistant", layout="wide")

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "main"

if "reviews" not in st.session_state:
    st.session_state.reviews = []

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("pesticides.csv")

df = load_data()

@st.cache_data
def load_regions():
    col = "Country" if "Country" in df.columns else "Area"
    return sorted(df[col].dropna().unique())

regions = load_regions()

# --------------------------------------------------
# TREND PLOT
# --------------------------------------------------
def plot_trend(start_year, end_year):
    temp = df[(df["Year"] >= start_year) & (df["Year"] <= end_year)]
    avg = temp.groupby("Year")["Value"].mean()

    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(avg.index, avg.values, marker="o", linewidth=3)
    ax.set_title("Pesticide Usage Trend", fontsize=18)
    ax.set_xlabel("Year", fontsize=14)
    ax.set_ylabel("Average Usage", fontsize=14)
    ax.grid(alpha=0.3)
    st.pyplot(fig)

# --------------------------------------------------
# GLOBAL STYLING
# --------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg,#e8f5e9,#f1f8e9,#e3f2fd,#fffde7);
    background-size: 400% 400%;
    animation: bg 12s ease infinite;
}
@keyframes bg {
    0%{background-position:0% 50%}
    50%{background-position:100% 50%}
    100%{background-position:0% 50%}
}

h1 { font-size:48px; }
h2 { font-size:36px; }
h3 { font-size:26px; }

.header {
    background:white;
    padding:18px 28px;
    border-radius:18px;
    box-shadow:0 10px 22px rgba(0,0,0,0.15);
    display:flex;
    justify-content:space-between;
    margin-bottom:30px;
}
.header span {
    padding:10px 22px;
    border-radius:22px;
    background:#e8f5e9;
    border:1px solid #c8e6c9;
    font-weight:600;
    font-size:16px;
}

.card {
    background:white;
    border-radius:18px;
    padding:28px;
    box-shadow:0 10px 22px rgba(0,0,0,0.15);
    margin-top:20px;
    font-size:18px;
    line-height:1.7;
}

/* 🔹 GLOBAL BUTTON SPACING */
div.stButton {
    margin-top: 18px;
}

/* BUTTON STYLING */
div.stButton > button {
    background: linear-gradient(135deg,#43a047,#2e7d32);
    color:white;
    font-size:20px;
    padding:0.9em 2.2em;
    border-radius:30px;
    border:none;
    box-shadow:0 10px 22px rgba(67,160,71,0.5);
    transition:0.3s;
}
div.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow:0 14px 26px rgba(67,160,71,0.7);
}

.footer {
    text-align:center;
    color:#2e7d32;
    font-size:18px;
    padding:30px 0;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<div class="header">
    <div style="font-size:26px;font-weight:bold;color:#2e7d32;">🌱 AgriSmart</div>
    <div style="display:flex;gap:14px;">
        <span>Home</span>
        <span>Blog</span>
        <span>Login</span>
        <span>Logout</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================================================
# MAIN PAGE
# ==================================================
if st.session_state.page == "main":

    st.markdown("<h1 style='text-align:center;'>🌾 AI Farm Management Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;font-size:22px;'>AI-powered pesticide prediction & farm advisory</p>", unsafe_allow_html=True)

    st.markdown("## 📥 Enter Farm Details")
    c1,c2,c3 = st.columns(3)
    with c1:
        region = st.selectbox("Country", regions)
    with c2:
        area = st.number_input("Area Code", min_value=0)
    with c3:
        year = st.number_input("Year", 1990, 2016)

    if st.button("🚜 Analyze Farm Data", use_container_width=True):
        pred = predict_pesticide_usage(area, year)
        colA,colB = st.columns(2)
        with colA:
            st.markdown(f"<div class='card'><b>Predicted Usage:</b> {round(pred,2)}</div>", unsafe_allow_html=True)
        with colB:
            ai = generate_farm_ai_response(pred, area, year)
            st.markdown(f"<div class='card'>{ai}</div>", unsafe_allow_html=True)

    st.markdown("## ✨ Key Features")
    st.markdown("""
    <div class="card">
     🤖 <b>ML-based prediction</b><br><br>
    🧠 <b>AI-powered recommendations</b><br><br>
    📊 <b>Historical data analysis (1990–2016)</b><br><br>
    🌱 <b>Sustainable farming focus</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🌾 Smart Farming Insights")
    st.markdown("""
    <div class="card">
                
    🚜 Precision Agriculture<br>
                
    💧 Soil & Water Protection<br>
                
    🐛 Pest Resistance Control<br>
                
    📈 Future-ready AI expansion
    </div>
    """, unsafe_allow_html=True)


    if st.button("🚀 Explore More", use_container_width=True):
        st.session_state.page = "explore"
        st.rerun()

    st.markdown("<div class='footer'>© 2025 AgriSmart</div>", unsafe_allow_html=True)

# ==================================================
# EXPLORE PAGE
# ==================================================
elif st.session_state.page == "explore":

    st.markdown("<h2 style='text-align:center;'>🚀 Explore More</h2>", unsafe_allow_html=True)
    col1,col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'><h3>📝 Feedback & Reviews</h3></div>", unsafe_allow_html=True)
        if st.button("Open Feedback", use_container_width=True):
            st.session_state.page = "feedback"
            st.rerun()

    with col2:
        st.markdown("<div class='card'><h3>🤖 AI Farm Assistant</h3></div>", unsafe_allow_html=True)
        if st.button("Open Chatbot", use_container_width=True):
            st.session_state.page = "chatbot"
            st.rerun()

    st.markdown("<div class='card'><h3>📊 Data & Visualization</h3></div>", unsafe_allow_html=True)
    if st.button("Open Visualization", use_container_width=True):
        st.session_state.page = "visualization"
        st.rerun()

    if st.button("⬅ Back to Home", use_container_width=True):
        st.session_state.page = "main"
        st.rerun()

# ==================================================
# FEEDBACK PAGE (FIXED PROPERLY)
# ==================================================
elif st.session_state.page == "feedback":

    st.markdown("<h2 style='text-align:center;'>📝 Farmer Feedback</h2>", unsafe_allow_html=True)

    with st.form("feedback_form"):
        pesticide = st.text_input("Pesticide Name")
        crop = st.selectbox("Crop", ["Wheat","Rice","Cotton","Maize","Vegetables"])
        rating = st.slider("Rating", 1, 5, 3)
        comment = st.text_area("Your Review")

        submitted = st.form_submit_button("Submit Feedback", use_container_width=True)

        if submitted:
            if pesticide.strip() and comment.strip():
                st.session_state.reviews.insert(0, {
                    "pesticide": pesticide,
                    "crop": crop,
                    "rating": rating,
                    "comment": comment
                })
                st.success("✅ Feedback submitted successfully!")
            else:
                st.warning("⚠️ Please fill all required fields.")

    # ---------------- SHOW REVIEWS ----------------
    if st.session_state.reviews:
        st.markdown("### ⭐ Recent Reviews")
        for r in st.session_state.reviews:
            stars = "★"*r["rating"] + "☆"*(5-r["rating"])
            st.markdown(f"""
            <div class='card'>
                <b>{r['pesticide']}</b> ({r['crop']})<br>
                {stars}<br><br>
                {r['comment']}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No reviews submitted yet.")

    if st.button("⬅ Back", use_container_width=True):
        st.session_state.page = "explore"
        st.rerun()


# ==================================================
# VISUALIZATION PAGE
# ==================================================
elif st.session_state.page == "visualization":

    st.markdown("<h2 style='text-align:center;'>📊 Data & Visualization Enhancements</h2>", unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    with c1:
        start = st.selectbox("From Year", list(range(1990,2017)))
    with c2:
        end = st.selectbox("To Year", list(range(1990,2017)), index=26)

    if st.button("📈 Generate Pesticide Trend", use_container_width=True):
        plot_trend(start, end)

    if st.button("⬅ Back", use_container_width=True):
        st.session_state.page = "explore"
        st.rerun()

# ==================================================
# CHATBOT PAGE
# ==================================================
elif st.session_state.page == "chatbot":

    st.markdown("<h2 style='text-align:center;'>🤖 AI Farm Assistant</h2>", unsafe_allow_html=True)
    q = st.text_area("Ask your question")

    if st.button("Generate Answer", use_container_width=True):
        if q.strip():
            ans = farm_chatbot_response(q)
            st.markdown(f"<div class='card'>{ans}</div>", unsafe_allow_html=True)

    if st.button("⬅ Back", use_container_width=True):
        st.session_state.page = "explore"
        st.rerun()
