import cv2
import easyocr
import re

# Initialize EasyOCR reader globally
reader = easyocr.Reader(['en'], gpu=False)

# Allowed card values
VALID_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def clean_ocr_text(raw_text):
    # Join all parts and remove symbols
    text = ''.join(filter(str.isalnum, raw_text.upper()))

    # Common OCR misreads
    text = text.replace('I', '1').replace('O', '0').replace('L', '1')

    # Replace known misreads like "1O", "IO", "I0", "LO" with "10"
    if re.fullmatch(r'[1IL][0O]', text):
        return '10'
    if re.fullmatch(r'10+', text):  # e.g., "100", "10O" → "10"
        return '10'

    # Handle two-letter reads like "KR", "K2", "QZ" → just take the first char
    if len(text) >= 2 and text[0] in 'JQKA':
        return text[0]

    # If text is fully valid, return it
    if text in VALID_VALUES:
        return text

    return ""  # fallback

def detect_value(card_img):
    # Convert to grayscale and enhance contrast
    gray = cv2.cvtColor(card_img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    h, w = enhanced.shape
    value_roi = enhanced[0:int(h * 0.25), 0:int(w * 0.25)]
    value_roi = cv2.resize(value_roi, (value_roi.shape[1]*2, value_roi.shape[0]*2))

    results = reader.readtext(value_roi, detail=0)
    raw_text = results[0] if results else ""

    value = clean_ocr_text(raw_text)

    print(f"Value: '{value}'")
    return value

