# Intentionally flawed Python program

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))

# shuffle the cards
random.shuffle(deck)

# Ensure there are enough cards to draw
if len(deck) < 5:
    raise ValueError("Not enough cards in the deck to draw five cards.")

# draw five cards
print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])
