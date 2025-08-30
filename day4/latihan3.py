import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = int(input())
computer = random.randint(1,3)

if player == 1:
    if computer == 1:
        print(f"{rock} vs {rock} Draw")
    elif computer == 2:
        print(f"{rock} vs {paper} You Lose")
    else:
        print(f"{rock} vs {scissors} You Win")


elif