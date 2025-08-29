print("Welcome to leap year check")
year = int(input("Year : "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")
    else:
        print(f"{year} is  leap year")
else:
    print(f"{year} is not leap year")