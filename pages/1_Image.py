import streamlit as st
import cv2
import numpy as np
from detector import detect_pedestrians

st.title("📷 Image Detection")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)  # BGR numpy array

    annotated_frame, count = detect_pedestrians(frame)

    st.image(annotated_frame, channels="BGR", caption=f"Detected {count} pedestrian(s)")
