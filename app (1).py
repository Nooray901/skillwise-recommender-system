
import streamlit as st
import pandas as pd

st.set_page_config(page_title="SkillWise Recommender", layout="centered")

# --- Hero Section ---
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>SkillWise: Personalized Learning Journey</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Smart course recommendations based on your progress and goals.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Course Selection & Recommendation ---
st.subheader("📘 Select a course you've completed:")

courses = {
    "Python for Beginners": ["Data Analysis with Pandas", "Intro to SQL", "Python Projects"],
    "Data Analysis with Pandas": ["Data Visualization", "Intermediate Python", "Statistics 101"],
    "Intro to SQL": ["Advanced SQL", "Database Design", "SQL for Data Science"],
    "Machine Learning A-Z": ["Deep Learning Basics", "AI for Business", "Python for ML"]
}

selected_course = st.selectbox("", list(courses.keys()))

if selected_course:
    st.success(f"✅ Course completed: {selected_course}")
    st.markdown("### 🎯 Recommended Next Courses:")
    for rec in courses[selected_course]:
        st.markdown(f"- {rec}")

# --- Post-Course Suggestion Banner ---
st.markdown("---")
st.markdown("#### 📌 Because you completed a course, we recommend you keep your momentum going:")
st.info("Next step: **Data Analysis with Pandas** is a great way to build on what you've just learned!")

# --- Skill Progress Tracker (Static Visual) ---
st.markdown("---")
st.markdown("### 📈 Skill Progress Tracker")

st.progress(60)
st.caption("You’ve completed 3 out of 5 beginner-level skills.")

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align: center;'>🚀 Powered by AI · Designed for Lifelong Learners</p>", unsafe_allow_html=True)
