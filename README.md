# Auto Rep Counter

Auto Rep Counter is a real-time bicep curl repetition counter built using **computer vision** and **machine learning** in Python.  
It uses a webcam feed and an **SVM classifier** to detect arm states (extended / contracted) and counts repetitions automatically.

---

## 🚀 Features
- Real-time webcam feed using OpenCV
- Image-based pose classification (Extended vs Contracted)
- Automatic rep counting using a state-machine approach
- Simple Tkinter GUI
- Train-your-own model with custom data
- Lightweight and easy to run locally

---

## 🧠 How It Works
1. Capture images for two classes:
   - **Extended arm**
   - **Contracted arm**
2. Train an SVM classifier on grayscale image data
3. Run real-time prediction on webcam frames
4. Count one rep for each **Extended → Contracted → Extended** cycle

---

## 🛠 Tech Stack
- Python
- OpenCV
- NumPy
- Scikit-learn (Linear SVM)
- Tkinter
- Pillow

---

## 📁 Project Structure
```
auto_rep_counter/
├── app.py
├── camera.py
├── model.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore

```
---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/RDharanish24/auto_rep_counter.git
cd auto_rep_counter
```
### 2️⃣ Install dependencies
```
pip install -r requirements.txt
```
## ▶️ Usage
### 1️⃣ Run the application
```
python main.py
```
### 2️⃣ Collect training data

Click Extended button to save extended-arm images

Click Contracted button to save contracted-arm images

Capture at least 20–30 images per class

### 3️⃣ Train the model
Click Train

### 4️⃣ Start counting reps
Click Toggle Counting

Perform bicep curls in front of the camera

---

## 📌 Notes
Ensure consistent lighting and camera angle

Stand clearly in front of the camera

Model performance improves with more training samples

## 🚧 Limitations
Pixel-based classification is sensitive to lighting and background

Not as accurate as pose-based methods

## 🔮 Future Improvements
MediaPipe pose-based angle detection

Model save/load functionality

Confidence score display

FPS counter

Support for additional exercises