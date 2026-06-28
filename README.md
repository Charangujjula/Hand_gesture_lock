> HAND GESTURE BASED LOCK / UNLOCK SYSTEM USING MEDIAPIPE AND STREAMLIT

This is a computer vision project where a user can unlock access using custom hand gestures (like 👊 ➡️ ☝️) detected in real time via webcam. But for now i have added only the images to show the lock as locked initially than unlock after the gesture.

--> FEATURES 
- Hand tracking & finger detection using MediaPipe
- Custom gesture password system
- Streamlit UI that displays real-time lock/unlock status
- Lightweight and easy to run

--> TECH STACK
- Python
- MediaPipe
- OpenCV
- Streamlit

--> HOW TO USE 

"Change the path of the lock unlock image in the app.py"

1. Run `detect_gesture.py` in one terminal  
2. Run `app.py` in another using `streamlit run app.py`  
3. Show the correct hand gesture pattern to unlock -- FIST👊 - INDEX☝️
