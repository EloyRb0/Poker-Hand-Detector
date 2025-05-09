import cardDetector
import handDetector
import winDetector

# ---- Main Execution ----
table_cards_1 = cardDetector.process_image('TableTest.jpeg', 5)     # Insert table photo
player_cards_1 = cardDetector.process_image('player1.jpeg', 2)   # Insert Player 1 hand
all_cards_1 = table_cards_1 + player_cards_1

best_hand_1 = handDetector.detect_hand(all_cards_1)
print(f"Best Hand Player 1: {best_hand_1}")

table_cards_2 = cardDetector.process_image('TableTest.jpeg', 5)     # Insert table photo as well
player_cards_2 = cardDetector.process_image('player2.jpeg', 2)   # Insert Player 2 hand
all_cards_2 = table_cards_2 + player_cards_2

best_hand_2 = handDetector.detect_hand(all_cards_2)
print(f"Best Hand Player 2: {best_hand_2}")

winner = winDetector.compare_hands(best_hand_1, best_hand_2)
print(f"Winner: {winner}")




