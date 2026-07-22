from ultralytics import YOLO

# Load once at import time — NOT inside a function that runs per-frame,
# otherwise every detection reloads the model from disk (slow).
model = YOLO("weights/yolo26n.pt")

def detect_pedestrians(frame):
    """
    frame: a single image as a numpy array (BGR, from OpenCV/webcam/video)
    returns: (annotated_frame, count) - image with boxes drawn, number of people found
    """
    results = model(frame, classes=[0])   # classes=[0] filters to "person" only
    annotated_frame = results[0].plot()   # ultralytics helper draws boxes/labels for you
    count = len(results[0].boxes)
    return annotated_frame, count
