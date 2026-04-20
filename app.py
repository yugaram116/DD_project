import streamlit as st
import cv2
import numpy as np
import av
import mediapipe as mp
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase, RTCConfiguration

st.set_page_config(page_title="Drowsiness Detection", layout="centered")

st.title("😴 Drowsiness Detection System")
st.write("Detects whether person is Active or Sleepy in real-time")

# MediaPipe setup
mp_face_mesh = mp.solutions.face_mesh

# Eye landmark indexes
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def eye_aspect_ratio(landmarks, eye):
    p1 = landmarks[eye[0]]
    p2 = landmarks[eye[1]]
    p3 = landmarks[eye[2]]
    p4 = landmarks[eye[3]]
    p5 = landmarks[eye[4]]
    p6 = landmarks[eye[5]]

    # EAR formula
    vertical1 = np.linalg.norm(np.array(p2) - np.array(p6))
    vertical2 = np.linalg.norm(np.array(p3) - np.array(p5))
    horizontal = np.linalg.norm(np.array(p1) - np.array(p4))

    ear = (vertical1 + vertical2) / (2.0 * horizontal)
    return ear


class DrowsinessProcessor(VideoProcessorBase):
    def __init__(self):
        self.face_mesh = mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True
        )
        self.counter = 0

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = self.face_mesh.process(rgb)

        status = "ACTIVE"
        color = (0, 255, 0)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = img.shape
                landmarks = []

                for lm in face_landmarks.landmark:
                    x, y = int(lm.x * w), int(lm.y * h)
                    landmarks.append((x, y))

                left_ear = eye_aspect_ratio(landmarks, LEFT_EYE)
                right_ear = eye_aspect_ratio(landmarks, RIGHT_EYE)
                ear = (left_ear + right_ear) / 2.0

                if ear < 0.25:
                    self.counter += 1
                else:
                    self.counter = 0

                if self.counter > 15:
                    status = "SLEEPY 😴"
                    color = (0, 0, 255)

                # Draw status
                cv2.putText(img, f"Status: {status}", (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

                cv2.putText(img, f"EAR: {ear:.2f}", (30, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        return av.VideoFrame.from_ndarray(img, format="bgr24")


RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

webrtc_streamer(
    key="drowsiness",
    video_processor_factory=DrowsinessProcessor,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)
