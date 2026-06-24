import streamlit as st
from agents.gemini_agent import ask_gemini

st.set_page_config(page_title="AI Career Mentor", page_icon="🤖")

st.title("🚀 AI Career Mentor (Kaggle Project)")
st.subheader("Your Smart AI Guide for Career, Resume & Roadmap")

# Sidebar
st.sidebar.title("👤 User Profile")
name = st.sidebar.text_input("Enter your name")
goal = st.sidebar.selectbox("Your Goal", ["Engineering", "MBBS", "Data Science", "Government Job", "Other"])

if name:
    st.sidebar.success(f"Welcome {name} 👋")

# Main input
user_input = st.text_area("Ask anything about career / resume / roadmap")

if st.button("Get AI Guidance"):
    if user_input:
        prompt = f"""
You are an expert Career Mentor AI.

User Name: {name}
Goal: {goal}

User Query: {user_input}

Give:
1. Simple explanation
2. Step-by-step roadmap
3. Skills required
4. Resume tips
5. Real-world project ideas
Make response beginner friendly.
"""
        response = ask_gemini(prompt)
        st.markdown("## 🤖 AI Response")
        st.write(response)
    else:
        st.warning("Please enter a question")