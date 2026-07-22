# 🚶 Pedestrian Detection with YOLO

A Streamlit app that detects pedestrians in images, videos, and a live webcam feed using [Ultralytics YOLO](https://github.com/ultralytics/ultralytics), containerized with Docker.

## Features

- **📷 Image** — upload a JPG/PNG and get back an annotated image with pedestrian count
- **🎥 Video** — upload an MP4/AVI/MOV and view frame-by-frame detection
- **🔴 Live Webcam** — real-time detection over WebRTC in the browser

All three modes share a single detector (`detector.py`) that loads the YOLO model once and filters detections to the "person" class.

## Project structure

```
.
├── app.py              # Streamlit entry point / landing page
├── detector.py         # YOLO model loading + person detection
├── pages/
│   ├── 1_Image.py       # Image upload page
│   ├── 2_Video.py       # Video upload page
│   └── 3_Webcam.py      # Live webcam page (streamlit-webrtc)
├── weights/              # YOLO weights (yolo26n.pt), downloaded at build/first run
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Running with Docker (recommended)

```bash
docker compose up --build
```

Then open [http://localhost:8501](http://localhost:8501).

Model weights are cached in a named Docker volume (`yolo-weights`) so they persist across container rebuilds.

## Running locally

```bash
pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt
streamlit run app.py
```

## Tech stack

- [Streamlit](https://streamlit.io/) — UI
- [Ultralytics YOLO](https://docs.ultralytics.com/) — object detection
- [OpenCV](https://opencv.org/) (headless) — image/video I/O
- [streamlit-webrtc](https://github.com/whitphx/streamlit-webrtc) — live webcam streaming
