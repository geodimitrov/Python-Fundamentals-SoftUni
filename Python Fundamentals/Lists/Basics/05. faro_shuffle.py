
cards = input().split()
num_shuffles = int(input())

# Use constants for top & bottom cards (they don't change)
TOP_CARD = cards[0]
BOTTOM_CARD = cards[-1]

# Copy the original list of cards, remove top & bottom, split in half
shuffled_cards = cards.copy()
shuffled_cards.remove(TOP_CARD)
shuffled_cards.remove(BOTTOM_CARD)
half = len(shuffled_cards) // 2

# "Shuffle" the cards
for shuffles in range(num_shuffles):
    
    shuffled_cards_new = []
    left_cards = shuffled_cards[0:half]
    right_cards = shuffled_cards[half:len(shuffled_cards)]
    
    for i in range(half):
        shuffled_cards_new.append(right_cards[i])
        shuffled_cards_new.append(left_cards[i])
    
    shuffled_cards = shuffled_cards_new
    
# Add top & bottom back to the list
shuffled_cards.append(BOTTOM_CARD)
shuffled_cards.insert(0, TOP_CARD)

print (shuffled_cards)

