# 👁️ Face Detection App using MTCNN and Streamlit

This project is a simple web application that detects human faces in an image using the **MTCNN (Multi-task Cascaded Convolutional Networks)** algorithm. It draws bounding boxes around faces and highlights facial keypoints like eyes, nose, and mouth.

Built with:
- 🐍 Python
- 📦 MTCNN
- 🖼 OpenCV
- 🌐 Streamlit (for web UI)

---

## 🚀 Demo

Live App: [Click Here to Try It Out]([https://your-app-url.streamlit.app](https://face20detection-exhjehtwkqm25w2awfesac.streamlit.app/))  
*(Replace with actual deployed link)*

---

## 📸 Features

- Upload any image (JPG, JPEG, PNG)
- Detect multiple faces
- Display:
  - Bounding box around faces
  - Keypoints for eyes, nose, and mouth
- Download the output image with annotations

---

## 📦 Installation

```bash
git clone https://github.com/your-username/face-detection-streamlit.git
cd face-detection-streamlit
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

The app will launch in your default browser at `http://localhost:8501`.

---

## 🌐 Deploy on Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click “New app” and connect your repo
4. Deploy and share your public link!

---

## 📁 File Structure

```
📦 face-detection-streamlit
 ┣ 📄 app.py                # Streamlit main app
 ┣ 📄 requirements.txt      # Python dependencies
 ┗ 📄 README.md             # Project info
```

---

## ✨ Example Output

| Input Image | Output with Face Detection |
|-------------|----------------------------|
|  ![vk](https://github.com/user-attachments/assets/9ca5938d-3b12-4d89-9a03-ae37d204bbe1)|

| <img width="915" height="723" alt="image" src="https://github.com/user-attachments/assets/e8c6e3d8-6473-4a0e-bf98-bcee9670ef1c" />|

---

## ✅ Requirements

```
streamlit
mtcnn
opencv-python
numpy
Pillow
```

---

## 🧠 How It Works

- `MTCNN` detects faces and facial keypoints.
- `OpenCV` draws rectangles and circles.
- `Streamlit` provides a drag-and-drop interface and displays output.

---

