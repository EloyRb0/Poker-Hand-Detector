import cv2
import cardDetector
import handDetector

# ---- Main Execution ----
table_cards = cardDetector.process_image('table.jpg', 5)     # Public cards
player_cards = cardDetector.process_image('player.jpg', 2)   # Player’s hand
all_cards = table_cards + player_cards

best_hand = handDetector.detect_hand(all_cards)
print(f"Best Hand: {best_hand}")

cv2.waitKey(0)
cv2.destroyAllWindows()