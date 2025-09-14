import json

data = []


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_symbol = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
symbols = ["♠", "♥", "♦", "♣"]

print(len(card_symbol))
print(len(cards))
for i in range(len(cards)):
    for n in symbols:
        print(f" {card_symbol[i]+n}, value {cards[i]}")
        data.append({"value": cards[i], "symbol": card_symbol[i]+n})

print(data)

with open('deck.py', 'w') as f:
    json.dump(data, f)