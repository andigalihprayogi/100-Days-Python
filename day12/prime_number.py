

def is_prime(num):
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print(f"{num} is not prime")
    else:
        print(f"{num} is prime")


is_prime(int(input("masukkan angka?")))
