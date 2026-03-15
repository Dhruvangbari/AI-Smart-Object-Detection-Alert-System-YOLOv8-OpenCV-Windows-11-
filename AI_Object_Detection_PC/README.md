# AI Object Detection System (PC - Windows 11)
# 🚀 AI Smart Object Detection & Alert System

An AI-powered real-time detection system built using Python, OpenCV, and YOLOv8.  
This project detects humans and vehicles from a live webcam feed, captures images, logs events with timestamps, and optionally triggers alerts.


Designed for:
- Engineering mini-projects
- Hackathons
- Computer Vision practice
- AI-based monitoring systems

---

## 🎯 Features

- Real-time human detection
- Vehicle detection (car, bus, truck, motorcycle)
- Automatic image capture on detection
- Detection logging with timestamps
- Optional alarm sound alert
- Lightweight YOLOv8 nano model
- Fully offline after first model download

---

## 🧠 Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- Multithreading for alert system

---

## 📂 Project Structure

AI_Object_Detection_PC/
│
├── main.py
├── detector.py
├── alert.py
├── config.py
├── requirements.txt
├── logs/
├── captures/
└── README.md

---

## ⚙️ Installation

1. Install Python 3.10 or later.
2. Clone the repository:
   git clone <your-repo-link>
3. Navigate to project folder:
   cd AI_Object_Detection_PC
4. Install dependencies:
   pip install -r requirements.txt
5. Run the system:
   python main.py

Note: On first run, YOLOv8 model will automatically download.

---

## 🖥 System Requirements

Minimum:
- Windows 11
- 8GB RAM
- Webcam

Recommended:
- NVIDIA GPU (for faster inference)

---

## 📸 How It Works

1. Webcam captures live feed.
2. YOLOv8 processes frames in real-time.
3. When a human or vehicle is detected:
   - Bounding box is drawn
   - Image is saved in /captures
   - Event is logged in /logs
   - Alarm sound plays (if enabled)

---

## 🔒 Ethical Use Notice

This project is intended strictly for educational and authorized use.  
Ensure compliance with privacy laws and regulations before deploying in real-world environments.

---

## 📈 Future Improvements

- Email or Telegram alerts
- Web-based dashboard
- Video recording mode
- Face blurring for privacy protection
- GPU acceleration optimization

---

## 👨‍💻 Author

Developed as an AI + Computer Vision learning project.
## Setup Instructions

1. Install Python 3.10+
2. Open Command Prompt in this folder
3. Install dependencies:
   pip install -r requirements.txt
4. Run:
   python main.py

First run will automatically download the YOLO model.

## Features
- Detects Humans & Vehicles
- Saves captured images
- Logs detections
- Optional alarm sound
