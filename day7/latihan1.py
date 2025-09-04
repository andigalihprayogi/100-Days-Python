import random

list_vocab = ['Accuse', 'Acquire', 'Broadcast', 'Complain', 'Determine']
i = 0
choice_vocab = random.choice(list_vocab)
print(choice_vocab)
answer = input("Input :")
list_name = []

for i in choice_vocab:
    if answer == i:
        print("Right")
        list_name.append(i)
    else:
        print("Wrong")
        list_name.append("_")
