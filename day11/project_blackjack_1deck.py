import random
import json
from art import logo


with open('deck.json', 'r') as f:
    data = json.load(f)


print(logo)


def counting_value(values):
    all_values = 0
    for value in values:
        all_values += value
    return all_values


def win_condition(my_value, computer_value):
    if my_value == computer_value:
        return "draw"
    elif my_value > 21:
        return "You lose"
    elif computer_value > 21:
        return "You win"
    elif my_value > computer_value:
        return "You Win"
    elif computer_value > my_value:
        return "You Lose"


GAME_START = True


while GAME_START:
    my_card_value = []
    my_card_symbol = []
    computer_card_value = []
    computer_card_symbol = []

    for i in range(2):
        my_card_index = random.randint(0, len(data))
        my_card = data.pop(my_card_index)
        my_card_value.append(my_card["value"])
        my_card_symbol.append(my_card["symbol"])
        computer_card_index = random.randint(0, len(data))
        computer_card = data.pop(computer_card_index)
        computer_card_value.append(computer_card["value"])
        computer_card_symbol.append(computer_card["symbol"])

    my_value_cards = counting_value(my_card_value)
    computer_value_card = counting_value(computer_card_value)

    print(f"computer card {computer_card_symbol[0]} ")
    print(f"Your card {my_card_symbol[0]} and {my_card_symbol[1]}")

    print(len(data))
    if input("you want 1 card again ? y or n").lower() == "y" and len(data) > 4:
        my_card_index = random.randint(0, 51)
        my_card = data.pop(my_card_index)
        my_card_value.append(my_card["value"])
        my_card_symbol.append(my_card["symbol"])

        my_value_cards = counting_value(my_card_value)
        print(f"Your card {my_card_symbol[0]}, {my_card_symbol[1]} and {my_card_symbol[2]}")
        result = win_condition(my_value_cards, computer_value_card)
    else:
        result = win_condition(my_value_cards, computer_value_card)

    print(len(data))
    print(f"{result}, with your value is {my_value_cards} and computer value is {computer_value_card}")
    print(f"your card {my_card_symbol[0]}, {my_card_symbol[1]} "
          f"and computer card {computer_card_symbol[0]}, {computer_card_symbol[1]}")
    if input("You want to play again? y or n").lower() == "n" or len(data) < 4:
        GAME_START = False
        print(f"card amount = {len(data)}")
