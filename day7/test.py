import random
import hangman_art
import hangman_word

list_vocab = hangman_word.word_list
live = 6
choice_vocab = random.choice(list_vocab).lower()
print(choice_vocab)
list_name = []
end_game = False

print(f"{hangman_art.logo}")

for count in choice_vocab:
    list_name.append("_")

while not end_game:
    if ''.join(list_name) == choice_vocab:
        print("you win")
        end_game = True
    else:
        answer = input("Input :")
        print(choice_vocab.find(answer))
        if int(choice_vocab.find(answer)) >= 0:
            for n in range(0, len(list_name)):
                if answer == choice_vocab[n]:
                    list_name[n] = choice_vocab[n]
            print(list_name)
        else:
            live -= 1
            print(hangman_art.stages[live])
            if live == 0:
                print(f"You Lose, The right answer is {choice_vocab} ")
                end_game = True
