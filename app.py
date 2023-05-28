import streamlit as st
import pytesseract
from PIL import Image
import os

# Function to extract text from image using OCR
def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

# Streamlit app
def main():
    st.title("Image Text Extraction")
    uploaded_files = st.file_uploader("Upload Image Files", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

    if uploaded_files:
        for file in uploaded_files:
            image = Image.open(file)
            text = extract_text_from_image(image)

            st.header("Uploaded Image")
            st.image(image, caption='Uploaded Image', use_column_width=True)
            st.write("Extracted Text:")
            st.write(text.split("-"))
            st.write("---")

# Run the app
if __name__ == '__main__':
    main()
