#Shean Rahman
#nhc2cv

def card_to_value(card):
    global value
    if (card == "T") or (card == "J") or (card == "Q") or (card == "K"):
        return 10
    elif card == "A":
            return 1
    else:
        return (int(card))


def hard_score(hand):
    hand_value = 0
    for card in hand:
        hand_value = hand_value + card_to_value(card)

    return hand_value


def soft_score(hand):
    hand_value = 0
    first_ace = True
    for card in hand:
        if card == "A" and first_ace:
            card_value = 11
            first_ace = False
        else:
            card_value = card_to_value(card)
        hand_value = hand_value + card_value
    return hand_value



