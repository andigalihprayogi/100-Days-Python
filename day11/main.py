from art import logo
from random import choice, randint


def print_card():
    print(your_card)
    print(computer_card[0])
    print(your_card_amount)


def condition_win():
    if your_card_amount > 21:
        print(f"You lose your card amount {your_card_amount} and computer amount {computer_card_amount}")
    elif computer_card_amount > 21:
        print(f"You Win your card amount {your_card_amount} and computer amount {computer_card_amount}")
    elif your_card_amount < computer_card_amount:
        print(f"You lose your card amount {your_card_amount} and computer amount {computer_card_amount}")
    elif your_card_amount == computer_card_amount:
        print(f"Draw your card amount {your_card_amount} and computer amount {computer_card_amount}")
    elif your_card_amount > computer_card_amount:
        print(f"You Win your card amount {your_card_amount} and computer amount {computer_card_amount}")


def card_add(card, card_amount):
    if card_amount > 10 and choice(cards) == 11:
        card.append(1)
        card_amount += 1
        return card_amount

    else:
        card.append(choice(cards))
        card_amount += card[-1]
        return card_amount


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_start = True
while game_start:
    your_card = []
    your_card_amount = 0
    computer_card = []
    computer_card_amount = 0
    computer_card_prob = randint(1, 6)

    print(logo)
    for i in range(2):
        your_card.append(choice(cards))
        computer_card.append(choice(cards))
        your_card_amount += your_card[i]
        computer_card_amount += computer_card[i]

    print_card()
    next_card = input("you want to take a card press'y' for yes press'n' for no? ")
    if next_card.lower() == 'y':
        your_card_amount = card_add(card=your_card, card_amount=your_card_amount)
        print_card()

    if computer_card_prob > 3 and computer_card_amount < 14:
        computer_card_amount = card_add(card=computer_card, card_amount=computer_card_amount)
        print_card()

    condition_win()
    next_game = input("if you want to continue the game press 'y' for yes, press 'n' for stop game")
    if next_game.lower() == 'n':
        game_start = False
