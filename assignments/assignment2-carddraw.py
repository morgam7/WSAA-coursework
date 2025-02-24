import requests

# Get a new shuffled deck
deck_url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
response = requests.get(deck_url)
deck_data = response.json()  # Convert JSON response to a dictionary

# Extract deck ID
deck_id = deck_data["deck_id"]

# Draw 2 cards from the deck
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
draw_response = requests.get(draw_url)
cards_data = draw_response.json()  # Convert JSON response to a dictionary

# Extract and print the value and suit of each drawn card
print("\nDrawn Cards:")
for card in cards_data["cards"]:
    print(f"{card['value']} of {card['suit']}")

