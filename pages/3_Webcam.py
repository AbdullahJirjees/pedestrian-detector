import streamlit as st
import av
from streamlit_webrtc import webrtc_streamer, RTCConfiguration
from detector import detect_pedestrians

st.title("🔴 Live Webcam Detection")

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    annotated_frame, _ = detect_pedestrians(img)
    return av.VideoFrame.from_ndarray(annotated_frame, format="bgr24")

webrtc_streamer(
    key="pedestrian-detection",
    video_frame_callback=video_frame_callback,
    rtc_configuration=RTC_CONFIGURATION,
)
