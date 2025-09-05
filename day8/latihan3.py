
# untuk cek bilangan prima
def prime_caker(number):
    if number == 2 or number == 3:
        print(f"{number} is prime")
    elif number <= 1:
        print(f"{number} is not prime")
    elif number % 2 == 0:
        print(f"{number} is not prime")
    elif number % 3 == 0:
        print(f"{number} is not prime")
    elif number % 5 == 0:
        print(f"{number} is not prime")
    elif number % 7 == 0:
        print(f"{number} is not prime")
    else:
        print(f'{number} is prime')

number_input = int(input("Masukkan angka :"))
prime_caker(number_input)
