
print("Welcome to BMI calculation, input your weight in kg(kilogram) and height in m(meter)")
def BMI_calculation(weight, height):
    BMI = round(weight/ height**2, 2)
    if BMI < 18.5:
        wieght_result = "Underweight"
    elif BMI <25.0:
        wieght_result = "Healthy Weight"
    elif BMI < 30:
        wieght_result = "Overweight"
    else:
        wieght_result = "Obesity"
    print(f"Your BMI(Body Mass Index) is {BMI} your {wieght_result}")

weight_person = float(input("input your weight? "))
height_person = float(input("input your height? "))
BMI_calculation(weight_person, height_person)
