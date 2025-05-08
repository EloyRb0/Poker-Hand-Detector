import cv2
import pytesseract

# PyTesseract route (if not added in PATH)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def detect_value(card_img):
    # grayscale conversion
    gray = cv2.cvtColor(card_img, cv2.COLOR_BGR2GRAY)

    # Crop top-left corner of the img (value)
    h, w = gray.shape
    value_roi = gray[0:int(h*0.25), 0:int(w*0.25)]

    # Apply thresholding for OCR accuracy
    _, thresh = cv2.threshold(value_roi, 120, 255, cv2.THRESH_BINARY_INV)

    # OCR config to limit recogintion to digits and letters
    config = r'--psm 10 -c tessedit_char_whitelist=0123456789JQKA'

    # Run Tesseract
    text = pytesseract.image_to_string(thresh, config=config)

    # Clean output
    value = text.strip().upper()

    # Basic correction
    if value == '0':
        value = '10'
    
    print(f'Detected value {value}')
    return value