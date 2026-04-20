# Driver Drowsiness Detection System

A real-time Driver Drowsiness Detection System built using OpenCV and MediaPipe Face Mesh.
This application monitors a user's facial features through a webcam to detect drowsiness, eye closure, and yawning, and triggers alerts to improve safety.

📌 Features
👁️ Eye Monitoring using Eye Aspect Ratio (EAR)
😮 Yawning Detection using Mouth Aspect Ratio (MAR)
⏱️ PERCLOS (Percentage of eye closure over time)
🔔 Real-time Audio & Visual Alerts
📊 Live HUD Metrics Display
🎥 Optional Video Recording
⚡ Lightweight (No dlib required)
🧠 How It Works

The system uses facial landmark detection to compute:

EAR (Eye Aspect Ratio)
Measures eye openness. If it falls below a threshold, eyes are considered closed.
MAR (Mouth Aspect Ratio)
Detects yawning based on mouth opening.
PERCLOS
Calculates the percentage of time eyes remain closed over a rolling window.
Higher values indicate fatigue.

🗂️ Project Structure

dd_project/
│
├── app.py                           # Streamlit web application
├── drowsiness_detector.py           # Main OpenCV-based detection system
├── drowsiness_detector_mediapipe.py # MediaPipe-based implementation
├── requirements.txt                 # Python dependencies
├── packages.txt                     # System dependencies (for deployment)
├── runtime.txt                      # Python version
└── README.md                        # Project documentation

⚙️ Installation

1. Clone the repository
git clone https://github.com/your-username/dd_project.git
cd dd_project
2. Install dependencies
pip install -r requirements.txt

▶️ Usage
Run OpenCV Version (Desktop)
python drowsiness_detector.py
Run Streamlit Web App
streamlit run app.py

🔧 Requirements
Add the following to requirements.txt:

streamlit
opencv-python-headless
mediapipe
numpy
scipy
pygame
streamlit-webrtc
av

☁️ Deployment (Streamlit Cloud)
packages.txt
libgl1
libglib2.0-0
libsm6
libxext6
libxrender1
Notes
Avoid using ffmpeg (can cause dependency conflicts)
Avoid outdated system libraries like libffi7, libpcre3

🚨 Alert Logic
WARNING → Eyes frequently closing
YAWNING → Mouth open for multiple consecutive frames
DROWSY → Eyes closed for extended duration or high PERCLOS

📊 Output Display
EAR value
MAR value
PERCLOS percentage
Alert status (AWAKE / WARNING / DROWSY / YAWNING)
Session duration and event counts

🛠️ Technologies Used
MediaPipe Face Mesh
OpenCV
Streamlit
Pygame (audio alerts)
NumPy & SciPy

⚠️ Limitations
Works best under good lighting conditions
Requires clear frontal face visibility
Thresholds may need tuning for different users

🚀 Future Improvements
Mobile deployment
Deep learning-based fatigue detection
Cloud-based monitoring and analytics
Multi-face support

👨‍💻 Author
Yugaram
Department of AI&DS

📜 License

This project is licensed under the MIT License.
