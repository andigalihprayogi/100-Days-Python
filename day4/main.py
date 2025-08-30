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

# Write your code below this line 👇

player = int(input("What's your choice (1)rock,(2) paper,(3) scissors?"))
computer = random.randint(1, 3)

if player == 1 and computer == 2:
    print(f"""
    Player choice {rock}
    vs
    computer choice {paper}
    You Lose
    """)
elif player == 1 and computer == 3:
    print(f"""
    Player choice {rock}
    vs
    computer choice {scissors}
    You Win
    """)
elif player == 1 and computer == 1:
    print(f"""
    Player choice {rock}
    vs
    computer choice {rock}
    You Draw
    """)
elif player == 2 and computer == 1:
    print(f"""
    Player choice {paper}
    vs
    computer choice {rock}
    You Win
    """)
elif player == 2 and computer == 2:
    print(f"""
    Player choice {paper}
    vs
    computer choice {paper}
    You Draw
    """)
elif player == 2 and computer == 3:
    print(f"""
    Player choice {paper}
    vs
    computer choice {scissors}
    You Lose
    """)
elif player == 3 and computer == 1:
    print(f"""
    Player choice {scissors}
    vs
    computer choice {rock}
    You Lose
    """)
elif player == 3 and computer == 2:
    print(f"""
    Player choice {scissors}
    vs
    computer choice {paper}
    You Win
    """)
elif player == 3 and computer == 3:
    print(f"""
    Player choice {scissors}
    vs
    computer choice {scissors}
    You Draw
    """)
else:
    print("you worng choice")
