# Intentionally flawed Python program

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14), ['Spades','Hearts','Diamonds','Clubs']))

# shuffle the cards
random.shuffle(deck)

def ascii_card(value_str, suit):
    """Return a string representing a card in ASCII art."""
    suit_symbols = {
        'Spades': '♠',
        'Hearts': '♥',
        'Diamonds': '♦',
        'Clubs': '♣'
    }
    symbol = suit_symbols.get(suit, '?')
    # Show only the first letter for face cards and Ace
    face_map = {"Ace": "A", "Jack": "J", "Queen": "Q", "King": "K"}
    if value_str in face_map:
        val = face_map[value_str]
    else:
        val = value_str[:2]
    lines = [
        "┌─────────┐",
        f"│{val:<2}       │",
        "│         │",
        f"│    {symbol}    │",
        "│         │",
        f"│       {val:>2}│",
        "└─────────┘"
    ]
    return "\n".join(lines)

print("You got:")
for i in range(5):
    value = deck[i][0]
    # Map special card values to names
    if value == 1:
        value_str = "Ace"
    elif value == 11:
        value_str = "Jack"
    elif value == 12:
        value_str = "Queen"
    elif value == 13:
        value_str = "King"
    else:
        value_str = str(value)
    suit = deck[i][1]
    print(f"{value_str} of {suit}")
    print(ascii_card(value_str, suit))
