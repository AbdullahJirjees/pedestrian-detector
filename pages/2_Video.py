import streamlit as st
import cv2
import tempfile
from detector import detect_pedestrians

st.title("🎥 Video Detection")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    tfile.write(uploaded_file.read())

    cap = cv2.VideoCapture(tfile.name)
    frame_placeholder = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        annotated_frame, count = detect_pedestrians(frame)
        frame_placeholder.image(annotated_frame, channels="BGR", caption=f"Detected {count} pedestrian(s)")

    cap.release()
