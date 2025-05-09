# Poker-Hand-Detector
This project allows you to **detect and compare two poker hands** from images using Python, OpenCV, and EasyOCR. It identifies table and player cards from images, evaluates the best possible poker hand for each player, and determines the winner.

---
## Features
- Detects cards from real images using OCR and image processing.
- Supports full Texas Hold'em hand detection (5 table cards + 2 player cards).
- Compares two players' hands and determines the winner.
---

## Technologies Used

- **Python 3**
- **OpenCV** – Image preprocessing and enhancement
- **EasyOCR** – Card value recognition via optical character recognition
- **NumPy** – Efficient array processing
- **itertools** – Combination logic for hand evaluation
- **re** – Regular expressions for text cleaning

---
## Getting Started
1. Clone the repository: \
   ``` git clone https://github.com/your-username/poker-hand-comparator.git ```
   ``` cd poker-hand-comparator ```
2. Install dependencies: \
   ``` pip install easyocr opencv-python numpy ```
3. Insert your own images in main.py (first move the image files to the directory)\
   ``` table_cards_1 = cardDetector.process_image('INSERT IMAGE NAME HERE', 5) # Insert table photo ``` \
   ``` player_cards_1 = cardDetector.process_image('INSERT IMAGE NAME HERE', 2)   # Insert Player 1 hand ``` \
   ``` ptable_cards_2 = cardDetector.process_image('INSERT IMAGE NAME HERE', 5)     # Insert table photo as well ``` \
   ``` player_cards_2 = cardDetector.process_image('INSERT IMAGE NAME HERE', 2)   # Insert Player 2 hand ```
   <br>Pre-tested images can be found at the test_Images directory
5. Run main.py

---
## Expected Outputs 
- Best Hand Player 1: (Highest poker hand formed)
- Best Hand Player 2: (Highest poker hand formed)
- Winner: (Player 1 / Player 2 / Tie)
---
## Supported Image Format
Table Photo:
![player1](https://github.com/user-attachments/assets/bcb32514-8195-4c4e-a95b-ecda824166bf)
Player Hand Photo:
![PokerTest](https://github.com/user-attachments/assets/a525107d-db3f-46d6-b9aa-bde36ead37a3)
---

