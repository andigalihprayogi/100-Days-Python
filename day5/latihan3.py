# number_sum = 0
#
# for number in range(1,101):
#     number_sum += number
#
# print(f"the total number is {number_sum}")

number_sum = 0
number_start = int(input("Masukkan angka awal :"))
number_input = int(input("Masukkan batasan angka :"))
step_number = int(input("Masukkan angka setiap stepnya :"))


for number in range(number_start,number_input+1, step_number):
    number_sum += number
    print(number)

print(f"the total number is {number_sum}")