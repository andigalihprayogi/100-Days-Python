number_start = int(input("Masukkan angka awal :"))
number_input = int(input("Masukkan batasan angka :"))
step_number = int(input("Masukkan angka setiap stepnya :"))
if step_number <= 0:
    print("angka step tidak boleh 0")
    quit()

for number in range(number_start, number_input+1, step_number):
    if number % 3 == 0 and number % 5 == 0 and number > 0:
        print("FIzzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
