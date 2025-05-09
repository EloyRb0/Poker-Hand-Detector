def compare_hands(hand1_rank: str, hand2_rank: str) -> str:
    # Define hand rankings in order
    hand_ranking_order = [
        "High Card", "Pair", "Two Pair", "Three of a Kind", "Straight",
        "Flush", "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"
    ]

    # Compare the ranks
    if hand_ranking_order.index(hand1_rank) > hand_ranking_order.index(hand2_rank):
        return "Player 1"
    elif hand_ranking_order.index(hand1_rank) < hand_ranking_order.index(hand2_rank):
        return "Player 2"
    else:
        return "It's a tie"
    