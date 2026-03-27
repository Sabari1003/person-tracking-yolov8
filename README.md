Real-Time Object Tracking using YOLOv8

📌 Overview
This project implements a real-time object tracking system using YOLOv8 and OpenCV. The system detects and tracks objects in a video by assigning unique IDs to each object across frames.

🚀 Features
Real-time object detection using YOLOv8
Object tracking with unique IDs (ByteTrack)
Optimized for faster performance
Works on video input

🛠️ Tech Stack
Python
OpenCV
YOLOv8 (Ultralytics)

⚙️ How It Works
Input video is processed frame-by-frame
YOLOv8 detects objects in each frame
Tracking algorithm assigns unique IDs
Objects are tracked continuously across frames

⚡ Optimization
Used lightweight model (YOLOv8n) for faster processing
Resized frames to improve speed

▶️ Run the Project
pip install ultralytics opencv-python
python track.py

📌 Future Improvements
Track specific object (target locking)
Improve accuracy with custom training
Real-time webcam tracking
👨‍💻 Author

Sabari Priyan G
