def detect_hand(cards: list[dict]) -> str:
    # Convert face to number
    face_to_num = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 11, 'Q': 12, 'K': 13, 'A': 14 
    }

    values = sorted([face_to_num[card['value']] for card in cards])
    suits = [card['suit'] for card in cards]

    val_counts = {}
    for v in values:
        if v in val_counts:
            val_counts[v] += 1
        else:
            val_counts[v] = 1

    counts = list(val_counts.values())
    is_flush = len(set(suits)) == 1
    is_straight = values == list(range(min(values), max(values)+1))

    if is_flush and values == [10, 11, 12, 13, 14]:
        return "Royal Flush"
    elif is_flush and is_straight:
        return "Straight Flush"
    elif 4 in counts:
        return "Four of a Kind"
    elif sorted(counts) == [2, 3]:
        return "Full House"
    elif is_flush:
        return "Flush"
    elif is_straight:
        return "straight"
    elif 3 in counts:
        return "Three of a Kind"
    elif counts.count(2) == 2:
        return "Two Pair"
    elif 2 in counts:
        return "Pair"
    else:
        return "High Card"