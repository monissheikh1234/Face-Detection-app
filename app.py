import streamlit as st
from mtcnn import MTCNN
import cv2
import numpy as np
from PIL import Image

# Title of the app
st.title("Face Detection using MTCNN")

# Upload image file
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert to OpenCV format
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)
    image_cv2 = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    # Face detection
    detector = MTCNN()
    output = detector.detect_faces(image_cv2)

    # Draw boxes and keypoints
    for face in output:
        x, y, width, height = face['box']
        keypoints = face['keypoints']

        # Draw face bounding box
        cv2.rectangle(image_cv2, (x, y), (x + width, y + height), (255, 0, 0), 3)

        # Draw facial keypoints
        for point in keypoints.values():
            cv2.circle(image_cv2, point, radius=2, color=(255, 0, 0), thickness=3)

    # Convert BGR to RGB for displaying in Streamlit
    result_image = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
    st.image(result_image, caption="Detected Faces", use_column_width=True)

    # Download button
    result_pil = Image.fromarray(result_image)
    st.download_button(label="Download Output Image", data=result_pil.tobytes(), file_name="output.jpg", mime="image/jpeg")
