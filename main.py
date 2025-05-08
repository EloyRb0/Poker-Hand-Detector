import cardDetector
import handDetector

# ---- Main Execution ----
table_cards = cardDetector.process_image('PokerTest.jpeg', 5)     # Public cards
player_cards = cardDetector.process_image('player2.jpeg', 2)   # Player’s hand
all_cards = table_cards + player_cards

best_hand = handDetector.detect_hand(all_cards)
print(f"Best Hand: {best_hand}")
