import random
import hangman_word

list_vocab = hangman_word.word_list
live = 3
choice_vocab = random.choice(list_vocab).lower()
list_name = []
end_game = False

random_number = random.randint(0, len(choice_vocab))

for n in choice_vocab:
    list_name.append(n)

list_name[random_number] = "_"
print(list_name)
while live > 0:
    quest = input("Masukkan huruf yang benar ?")
    list_name[random_number] = quest
    print(list_name)
    print(''.join(list_name))
    if ''.join(list_name) == choice_vocab:
        print(" you win")
    else:
        live -= 1
        print("Try Again")

if live == 0:
    print("You Lose")