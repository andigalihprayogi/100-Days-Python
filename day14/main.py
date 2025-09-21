from game_data import data
from art import logo, vs
from random import choice


def print_question():
    print(f"{a_choice['name']}, {a_choice['description']}, from {a_choice['country']}")
    print(vs)
    print(f"{b_choice['name']}, {b_choice['description']}, from {b_choice['country']}")


def right_answer_incres_score(answer_score):
    answer_score += 1
    print(f"You're right! Current score: {answer_score}")


right_amswer = 0
game_start = True
a_choice = choice(data)
b_choice = choice(data)

while game_start:
    print(logo)
    print_question()
    while a_choice == b_choice:
        b_choice = choice(data)
    user_answer = input("Who has more followers? Type'A' or 'B'")
    if user_answer.upper() == 'A' and a_choice['follower_count'] > b_choice['follower_count']:
        right_answer_incres_score(answer_score=right_amswer)
        b_choice = choice(data)
    elif user_answer.upper() == 'B' and a_choice['follower_count'] < b_choice['follower_count']:
        right_answer_incres_score(answer_score=right_amswer)
        a_choice = b_choice
        b_choice = choice(data)
    else:
        print(f"Sorry that's wrong, final score {right_amswer}")
        right_amswer = 0
        game_start = False
