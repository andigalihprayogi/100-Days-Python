alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
start_program = True


def cesar_ciper(choice, input_text, move):
    new_word = ""
    if choice.lower() == "decode":
        move *= -1
    for i in input_text:
        if i not in alphabet:
            new_word += i
        else:
            number_index = alphabet.index(i)
            number_index += move
            abs(number_index)
            index_modulo = number_index % len(alphabet)
            new_word += alphabet[index_modulo]
    print(new_word)


while start_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cesar_ciper(choice=direction, input_text=text, move=shift)
    answer = input("You want to contine program (yes,no)?")
    if answer.lower() == "no":
        start_program = False
