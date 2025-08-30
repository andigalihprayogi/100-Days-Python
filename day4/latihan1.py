import random

random_result = random.randint(1,2)
player_input = int(input("(1) for Tail (2) for head? "))

if player_input == random_result:
    print(f"You win")
else:
    print(f"You Lose answer is {random_result}")