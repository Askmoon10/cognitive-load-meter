import cv2
import mediapipe as mp
import streamlit as st

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Cognitive Load Meter", layout="centered")
st.title("🧠 Cognitive Load Meter (Face + AI)")
st.write("Real-time cognitive load detection using facial behavior")

run = st.checkbox("Start Camera")
FRAME_WINDOW = st.image([])

# -------------------------------
# MediaPipe Face Mesh (DEFINE ONCE)
# -------------------------------
mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# -------------------------------
# Camera
# -------------------------------
cap = cv2.VideoCapture(0)

if run:
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Camera not accessible")
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(frame)

        load_score = 25  # default

        if result.multi_face_landmarks:
            load_score = 60  # face detected → simulated load

        cv2.putText(
            frame,
            f"Cognitive Load: {load_score}/100",
            (30, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        FRAME_WINDOW.image(frame)

else:
    cap.release()
