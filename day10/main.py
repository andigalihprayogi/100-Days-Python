from art import logo


def next_operation(number1, number2, operat):
    answer = 0
    if operation == "+":
        answer = number1 + number2
    elif operation == "-":
        answer = number1 - number2
    elif operation == "*":
        answer = number1 * number2
    elif operation == "/":
        if number2 == 0:
            print(f"second number can't zero")
        else:
            answer = number1/number2
    print(f"{number1} {operat} {number2} = {answer}")
    return answer


start_p = True
while start_p:
    print(logo)
    first_number = int(input("What's the first number? "))
    start_prog = True
    while start_prog:
        operation = input("+\n-\n*\n/\nPick on operation: ")
        second_number = int(input("What's the second number? "))
        first_number = next_operation(number1=first_number, number2=second_number, operat=operation)
        next_opera = input(f'Type "y" to continue calculation with {first_number}. or type"n" to start new calculation:'
                           f'If you want to the program type "yy"')
        if next_opera.lower() == "n":
            start_prog = False
        elif next_opera.lower() == "yy":
            start_prog = False
            start_p = False
