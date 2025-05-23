# Intentionally flawed Python program

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14), ['Spades','Hearts','Diamonds','Clubs']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
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
    print(value_str, "of", deck[i][1])
