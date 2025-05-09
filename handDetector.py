from itertools import combinations

def detect_hand(cards: list[dict]) -> str:

    face_to_num = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 11, 'Q': 12, 'K': 13, 'A': 14 
    }
    # Detect the best hand from a dictionary of 7 cards
    def evaluate_hand(five_cards):
        values = sorted([face_to_num[card['value']] for card in five_cards])
        suits = [card['suit'] for card in five_cards]

        val_counts = {}
        for v in values:
            val_counts[v] = val_counts.get(v, 0) + 1

        counts = list(val_counts.values())
        is_flush = len(set(suits)) == 1
        is_straight = values == list(range(min(values), max(values)+1))

        if is_flush and values == [10, 11, 12, 13, 14]:
            return 10, "Royal Flush"
        elif is_flush and is_straight:
            return 9, "Straight Flush"
        elif 4 in counts:
            return 8, "Four of a Kind"
        elif sorted(counts) == [2, 3]:
            return 7, "Full House"
        elif is_flush:
            return 6, "Flush"
        elif is_straight:
            return 5, "Straight"
        elif 3 in counts:
            return 4, "Three of a Kind"
        elif counts.count(2) == 2:
            return 3, "Two Pair"
        elif 2 in counts:
            return 2, "Pair"
        else:
            return 1, "High Card"

    best_rank = 0
    best_hand = ""

    for combo in combinations(cards, 5):
        rank, name = evaluate_hand(combo)
        if rank > best_rank:
            best_rank = rank
            best_hand = name

    return best_hand
