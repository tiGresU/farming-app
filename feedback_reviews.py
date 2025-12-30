import streamlit as st

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Pesticide Feedback & Reviews",
    layout="centered"
)

# --------------------------------------------------
# SESSION STATE TO STORE REVIEWS
# --------------------------------------------------
if "reviews" not in st.session_state:
    st.session_state.reviews = []

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #f4fff4;
}

/* Main Feedback Card */
.feedback-card {
    background: white;
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0 12px 25px rgba(0,0,0,0.15);
    max-width: 700px;
    margin: auto;
}

/* Submit Button Styling */
div.stButton > button {
    background: linear-gradient(135deg, #43a047, #2e7d32);
    color: white;
    font-size: 18px;
    padding: 0.7em 1.6em;
    border-radius: 30px;
    border: none;
    box-shadow: 0 8px 20px rgba(67,160,71,0.6);
    transition: all 0.3s ease-in-out;
}

div.stButton > button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 20px rgba(67,160,71,0.9);
}

/* Review Card */
.review-card {
    background: #ffffff;
    border: 1px solid #c8e6c9;
    border-radius: 14px;
    padding: 20px;
    margin-top: 18px;
    box-shadow: 0 6px 14px rgba(0,0,0,0.12);
    animation: fadeIn 0.6s ease-in;
    transition: transform 0.3s ease;
}

.review-card:hover {
    transform: translateY(-6px);
}

/* Star Style */
.star {
    font-size: 22px;
    color: #c8e6c9;
    transition: color 0.2s;
}

.star.active {
    color: #fbc02d;
}

/* Fade Animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.markdown(
    "<h2 style='text-align:center;color:#2e7d32;'>🌾 Feedback & Reviews</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Share your experience with pesticide effectiveness</p>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# FEEDBACK FORM (INSIDE CARD)
# --------------------------------------------------
st.markdown('<div class="feedback-card">', unsafe_allow_html=True)

pesticide = st.text_input("🧪 Pesticide Name")
crop = st.selectbox("🌱 Crop Name", ["Wheat", "Rice", "Cotton", "Maize", "Vegetables"])
rating = st.slider("⭐ Rating", 1, 5, 3)
comment = st.text_area("📝 Review / Effectiveness Comment")

submitted = st.button("Submit Review")

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------------------------------
# HANDLE SUBMISSION
# --------------------------------------------------
if submitted:
    if pesticide.strip() == "" or comment.strip() == "":
        st.warning("Please fill all required fields.")
    else:
        st.session_state.reviews.insert(0, {
            "pesticide": pesticide,
            "crop": crop,
            "rating": rating,
            "comment": comment
        })
        st.success("Review submitted successfully!")

# --------------------------------------------------
# DISPLAY REVIEWS
# --------------------------------------------------
st.markdown("### 🗣 Farmer Reviews")

for review in st.session_state.reviews:
    stars_html = ""
    for i in range(1, 6):
        if i <= review["rating"]:
            stars_html += '<span class="star active">★</span>'
        else:
            stars_html += '<span class="star">★</span>'

    st.markdown(f"""
    <div class="review-card">
        <b>🧪 Pesticide:</b> {review["pesticide"]}<br>
        <b>🌱 Crop:</b> {review["crop"]}<br><br>
        {stars_html}<br><br>
        <i>{review["comment"]}</i>
    </div>
    """, unsafe_allow_html=True)
