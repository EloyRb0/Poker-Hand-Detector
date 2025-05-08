import cv2
import numpy as np
import cardDetector
import valueDetector
import handDetector

# Main Program
img = cv2.imread('PokerTest.jpeg')
img = cv2.resize(img, (1000, 1000))  # Resize for consistency
imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# White mask for detecting card backgrounds 
white_low = np.array([0, 0, 200])
white_high = np.array([180, 50, 255])
white_mask = cardDetector.maskApplication(white_low, white_high, imgHsv)

# Clean mask with morphology
kernel = np.ones((5, 5), np.uint8)
white_mask = cv2.morphologyEx(white_mask, cv2.MORPH_CLOSE, kernel)

# Detect edges and find contours
edges = cv2.Canny(white_mask, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

card_contours = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 10000:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            card_contours.append(approx)

cards = []
# Extract and process each card
for i, card in enumerate(card_contours):
    warped_card = cardDetector.four_point_transform(img, card.reshape(4, 2))
    
    # Show or save the card
    cv2.imshow(f'Card {i+1}', warped_card)
    cv2.imwrite(f'card_{i+1}.jpg', warped_card)
    
    card_val = valueDetector.detect_value(warped_card) 
    suit = 'd' # suit simulado
    cards.append({"value": card_val, "suit": suit})

#handDetector.detect_hand(cards)
cv2.waitKey(0)
cv2.destroyAllWindows()