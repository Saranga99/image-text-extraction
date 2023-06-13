import streamlit as st
import pytesseract
import numpy as np
from PIL import Image
import os
import cv2
import easyocr

# Function to extract text from image using pytesseract OCR
def extract_text_with_pytesseract(image):
    text = pytesseract.image_to_string(image)
    return text

# Function to extract text from image using EasyOCR library
def extract_text_with_easyocr(image):
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image)
    text = ' '.join([result[1] for result in results])
    return text

# Function to extract text from image using OpenCV for specific text extraction techniques
def extract_text_with_opencv(image):
    image_array = np.array(image)
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(binary)
    return text

# Streamlit app
def main():
    st.title("Image Text Extraction")
    uploaded_files = st.file_uploader("Upload Image Files", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

    if uploaded_files:
        extraction_methods = {
            "Pytesseract": extract_text_with_pytesseract,
            "EasyOCR": extract_text_with_easyocr,
            "OpenCV": extract_text_with_opencv,
            # Add more extraction methods here
        }

        for file in uploaded_files:
            image = Image.open(file)

            st.header("Uploaded Image")
            st.image(image, caption='Uploaded Image', use_column_width=True)
            st.write("Extracted Text:")
            
            for method_name, extraction_method in extraction_methods.items():
                try:
                    text = extraction_method(image)
                    st.subheader(f"Extraction Method: {method_name}")
                    st.write(text)
                    st.write("---")
                except Exception as e:
                    st.error(f"Error extracting text using {method_name}: {str(e)}")
                    st.write("---")

# Run the app
if __name__ == '__main__':
    main()
