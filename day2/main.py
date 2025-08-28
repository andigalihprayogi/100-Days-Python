print("Welcome to the calculator tip")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
each_people_pay = (bill*(1+tip/100))/people
final_amount = "{:.2f}".format(each_people_pay)
print(f"Each person should pay: ${final_amount}")
