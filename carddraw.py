import requests
from collections import Counter

# Get a new shuffled deck
deck_url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
response = requests.get(deck_url)
deck_data = response.json()  # Convert JSON response to a dictionary


# Extract deck ID - this is in deck_data
deck_id = deck_data["deck_id"]

# Draw 5 cards from the deck
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
draw_response = requests.get(draw_url)
cards_data = draw_response.json()  # Convert JSON response to a dictionary


# Extract and print the value and suit of each drawn card - got 'value' and 'suit' fields from checking card_data
print("Drawn Cards:")
for card in cards_data["cards"]:
    print(f"{card['value']} of {card['suit']}")

# extracting list of the values and suits so I can count them
values = [card["value"] for card in cards_data["cards"]]
suits = [card["suit"] for card in cards_data["cards"]]

# Count repeated values and suits need to use counter to get the count of unique values
value_counts = Counter(values)
suit_counts = Counter(suits)

# Check for pair / triple and flush
good_hand = False

if 3 in value_counts.values():
    print("Congratulations, you got a triple!")
    good_hand = True
elif 2 in value_counts.values():
    print("Congratulations, you got a pair!")
    good_hand = True

if len(suit_counts) == 1:
    print("Congratulations, all 5 cards are the same suit (a flush)!")
    good_hand = True

if good_hand == False:
    print("Sorry, no pair, triple, or flush this time.")