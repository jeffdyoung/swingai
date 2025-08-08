import streamlit as st
import os
from analyzer import analyze_swing

SAMPLE_DIR = "sample_videos"
MY_DIR = "my_videos"

st.title("Golf Swing Analyzer")

user_video = st.selectbox("Choose your video:", os.listdir(MY_DIR))
sample_video = st.selectbox("Choose a sample video:", os.listdir(SAMPLE_DIR))

if st.button("Run Comparison"):
    user_path = os.path.join(MY_DIR, user_video)
    sample_path = os.path.join(SAMPLE_DIR, sample_video)
    output_path = analyze_swing(user_path, sample_path)
    st.video(output_path)
