# 🚗 Vehicle Detection and Counting System  

A computer vision project that detects and counts vehicles in video streams using **Python** and **OpenCV**. This system is useful for traffic monitoring, smart city applications, and automated vehicle statistics collection.  

---

## ✨ Features  
- Detects vehicles using **Background Subtraction (MOG2)**  
- Tracks and identifies vehicles with bounding boxes  
- Counts vehicles crossing a predefined **counting line**  
- Works with both **video files** and **live camera feeds**  
- Adjustable parameters for detection line and object size  

---

## 🛠️ Tech Stack  
- **Python 3.x**  
- **OpenCV (cv2)**  
- **NumPy**  

---

## 📌 How It Works  
1. The video feed is captured using OpenCV (`cv2.VideoCapture`).  
2. **Background subtraction** is applied to detect moving vehicles.  
3. Vehicles are filtered using a minimum width/height threshold.  
4. The **center point** of each vehicle is tracked.  
5. When a vehicle’s center crosses the defined line, it is counted.  

---


🎥 Example

Input: Traffic video footage

Output: Count of vehicles crossing the line displayed on screen



🔮 Future Improvements

Add speed estimation for vehicles

Classify vehicles into cars, bikes, buses, trucks

Integrate with a real-time dashboard for analytics
