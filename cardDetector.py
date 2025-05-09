import cv2
import numpy as np
import valueDetector

# Function to apply HSV mask
def maskApplication(lower, upper, image):
    mask = cv2.inRange(image, lower, upper)
    return mask

# Function to order contour points consistently
def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]      # Top-left
    rect[2] = pts[np.argmax(s)]      # Bottom-right

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]   # Top-right
    rect[3] = pts[np.argmax(diff)]   # Bottom-left

    return rect

# Function to warp perspective
def four_point_transform(image, pts, output_size=(200, 300)):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = int(max(widthA, widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = int(max(heightA, heightB))

    dst = np.array([
        [0, 0],
        [output_size[0] - 1, 0],
        [output_size[0] - 1, output_size[1] - 1],
        [0, output_size[1] - 1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, output_size)

    return warped

# Function to process the image and detect cards
def process_image(img_path, expected_cards):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (1000, 1000))
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    white_low = np.array([0, 0, 200])
    white_high = np.array([180, 50, 255])
    white_mask = maskApplication(white_low, white_high, imgHsv)

    kernel = np.ones((5, 5), np.uint8)
    white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_CLOSE, kernel)

    edges = cv2.Canny(white_mask, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    card_contours = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 10000:
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            if len(approx) == 4:
                card_contours.append(approx)

    # Sort by area if more than needed are detected
    if len(card_contours) > expected_cards:
        card_contours = sorted(card_contours, key=cv2.contourArea, reverse=True)[:expected_cards]

    cards = []
    for i, card in enumerate(card_contours):
        warped_card = four_point_transform(img, card.reshape(4, 2))

        value = valueDetector.detect_value(warped_card)
        suit = 'd'  # Replace with suit detector
        cards.append({'value': value, 'suit': suit})
    
    return cards