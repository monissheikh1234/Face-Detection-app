# 📸 Face Detection App

A simple yet stylish **web app** built with **Streamlit** and **OpenCV** that allows users to upload an image and detect human faces in it instantly. Users can switch between **Colorful** and **Dark** themes for a better visual experience.

---

## 🌟 Features

- 🎨 Theme toggle between Colorful and Dark Mode  
- 🖼️ Upload images in JPG, JPEG, or PNG format  
- 🤖 Face detection using Haar Cascade classifier from OpenCV  
- 📤 Download the processed image with detected face(s)  
- 💡 Clean and modern UI with bordered upload section  

---

## 🚀 Demo

To run the app locally:

```bash
streamlit run app.py
```

---

## 📂 File Structure

```
Face-Detection-app/
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md             # Project description
├── .streamlit/           # (Optional) Streamlit config files
└── .devcontainer/        # (Optional) VSCode Dev Container setup
```

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/monissheikh1234/Face-Detection-app.git
cd Face-Detection-app
```

2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the app**
```bash
streamlit run app.py
```

---

## 📦 Requirements

- Python 3.7+
- OpenCV
- Streamlit
- NumPy
- Pillow

All dependencies are listed in `requirements.txt`.

---

## 📸 Face Detection Logic

The face detection is implemented using OpenCV's Haar Cascade Classifier:

```python
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=4)
```

It detects all human faces in the uploaded image and draws bounding boxes.

---

## 💡 Screenshots

| 📤 Upload Image | ✅ Detected Face(s) |
|-----------------|--------------------|
|![Screenshot 2025-07-15 233203](https://github.com/user-attachments/assets/66173c0e-c0b9-43c0-aa8d-81e8e847308d)
 |![detected_faces (1)](https://github.com/user-attachments/assets/998d2eb3-012f-4529-a0b8-1dc9180ce7e6)
 |


---

## ✨ Contributing

Pull requests are welcome. Feel free to open issues and contribute improvements or new features!

---

## 👤 Author

**Monis Sheikh**  
🔗 [GitHub](https://github.com/monissheikh1234)

---
