from random import randint

random_nuber = randint(1, 100)
game_mode = input("chosee easy or hard mode?")


def game_run(life_player):
    while life_player > 0:
        guess = int(input("Input your number guess? "))
        if guess > random_nuber:
            print("number guess is to high")
            life_player -= 1
            print(f"your life is {life_player}")
        elif guess < random_nuber:
            print("number guess is to low")
            life_player -= 1
            print(f"your life is {life_player}")
        elif guess == random_nuber:
            print(f"you got the number {random_nuber}, You Win")
            break
    if life_player == 0:
        print("Your lose")


if game_mode.lower() == "easy":
    life = 10
    game_run(life)
else:
    life = 5
    game_run(life)
