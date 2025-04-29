
import streamlit as st
import pandas as pd

# Sample course data
courses = {
    "Python for Beginners": ["Data Analysis with Pandas", "Intro to SQL", "Python Projects"],
    "Data Analysis with Pandas": ["Data Visualization", "Intermediate Python", "Statistics 101"],
    "Intro to SQL": ["Advanced SQL", "Database Design", "SQL for Data Science"],
    "Machine Learning A-Z": ["Deep Learning Basics", "AI for Business", "Python for ML"]
}

# Streamlit UI
st.title("SkillWise: Course Recommender")

selected_course = st.selectbox("Select a course you've completed:", list(courses.keys()))

if selected_course:
    st.subheader("Recommended Next Courses:")
    for rec in courses[selected_course]:
        st.markdown(f"- {rec}")
