import streamlit as st
import cv2
import numpy as np
import time

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(
    page_title="Cognitive Load Meter",
    layout="centered"
)

st.title("🧠 Cognitive Load Meter (Cloud Demo)")
st.write(
    "This is a cloud-safe demo version of the Cognitive Load Meter.\n\n"
    "⚠️ **Live face detection (MediaPipe + Camera) is disabled on Streamlit Cloud** "
    "due to Python 3.12 limitations.\n\n"
    "👉 Full real-time demo runs locally."
)

st.warning(
    "MediaPipe & webcam access are not supported on Streamlit Cloud. "
    "This version demonstrates UI, logic, and simulated cognitive load."
)

# -------------------------------
# Simulated Cognitive Load Logic
# -------------------------------
st.subheader("📊 Cognitive Load Simulation")

start = st.button("Start Monitoring")

placeholder = st.empty()
progress_bar = st.progress(0)

if start:
    load_score = 20  # initial load
    for i in range(100):
        # Simulate cognitive load changes
        load_score = np.clip(load_score + np.random.randint(-3, 6), 0, 100)

        placeholder.metric(
            label="Cognitive Load Score",
            value=f"{load_score} / 100"
        )

        progress_bar.progress(load_score / 100)
        time.sleep(0.1)

    st.success("Monitoring completed!")

# -------------------------------
# Explanation Section
# -------------------------------
st.markdown("---")
st.subheader("🧩 How it works (Full Version)")

st.markdown(
    """
- Webcam captures live video  
- MediaPipe Face Mesh extracts facial landmarks  
- Eye movement, blink rate & facial tension are analyzed  
- Cognitive load score is computed in real-time  

🔒 **Cloud Limitation**  
Streamlit Cloud uses Python 3.12, which does not support MediaPipe.

💻 **Local Execution**  
Run this project locally to see the full real-time AI vision pipeline.
"""
)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Hackathon Project • Cognitive Load Meter • Face + AI")

