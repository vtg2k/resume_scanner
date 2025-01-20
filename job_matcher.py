import streamlit as st
import pandas as pd

st.title("AI Resume Screener")
st.sidebar.header("Upload Resume")
uploaded_file = st.sidebar.file_uploader("Choose a resume", type=["pdf", "docx"])

if uploaded_file:
    st.write("Processing resume...")
    # Call Flask API for processing (or use local function)
    st.write("Resume processed successfully!")