import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile

# Theme Selector
theme = st.selectbox("🎨 Select Theme", ["🌈 Colorful Theme", "🌙 Dark Theme"])

# Apply background styles
def set_background(theme):
    if theme == "🌈 Colorful Theme":
        st.markdown("""
        <style>
        .stApp {
            background-color: #99c8cc !important;
            color: #000000 !important;
            font-weight: 600;
        }
        </style>
        """, unsafe_allow_html=True)
    elif theme == "🌙 Dark Theme":
        st.markdown("""
        <style>
        .stApp {
            background-color: #121212 !important;
            color: rgba(255, 255, 255, 0.95) !important;
            font-weight: bold !important;
        }
        h1, h2, h3, h4, h5, h6, label, div, p, span {
            color: rgba(255, 255, 255, 0.97) !important;
            font-weight: bold !important;
        }
        .css-1offfwp, .css-q8sbsg, .css-hxt7ib {
            color: rgba(255, 255, 255, 0.97) !important;
            font-weight: bold !important;
        }
        </style>
        """, unsafe_allow_html=True)

set_background(theme)

# Dynamic colors
title_color = "#2C3E50" if theme == "🌈 Colorful Theme" else "#FFFFFF"
subtitle_color = "#1e272e" if theme == "🌈 Colorful Theme" else "#DDDDDD"
detect_color = "#ff5733" if theme == "🌈 Colorful Theme" else "#f1c40f"
border_color = "#ffffff80" if theme == "🌙 Dark Theme" else "#00000030"

# Border Styling Block
st.markdown(f"""
<div style="
    border: 2px solid {border_color};
    border-radius: 10px;
    padding: 25px 20px;
    margin-bottom: 30px;
    background-color: rgba(255, 255, 255, 0.03);
">
    <h1 style='text-align:center; color:{title_color}; font-weight: bold;'>📸 Face Detection App</h1>
    <h4 style='text-align:center; color:{subtitle_color};'>Upload an image and detect human faces using OpenCV</h4>
    <br/>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

# Close the bordered block
st.markdown("</div>", unsafe_allow_html=True)

# Load face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img_array, (x, y), (x+w, y+h), (255, 0, 0), 2)

    st.markdown(f"<h5 style='color:{detect_color}; font-weight: bold;'>✅ Detected {len(faces)} face(s)</h5>", unsafe_allow_html=True)
    st.image(img_array, caption="🖼️ Output Image", use_column_width=True)

    # Prepare for download
    result_image = Image.fromarray(img_array)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        result_image.save(tmp_file.name)
        with open(tmp_file.name, "rb") as file:
            st.download_button(
                label="⬇️ Download Output Image",
                data=file,
                file_name="detected_faces.jpg",
                mime="image/jpeg"
            )
