from main import MENU, resources

money = 0
mechine_start = True
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']


def is_resource_sufficient(order_ingredi, water_ing, milk_ing, coffee_ing):
    if order_ingredi["water"] > water_ing:
        print(f"​Sorry there is not enough water.")
        return False
    elif order_ingredi["milk"] > milk_ing:
        print(f"​Sorry there is not enough mlik.")
        return False
    elif order_ingredi["coffee"] > coffee_ing:
        print(f"​Sorry there is not enough coffee.")
        return False
    return True


def coffee_machine(order, payment, water_m, milk_m, coffee_m):
    if payment > MENU[order]['cost']:
        water_m -= MENU[order]['ingredients']['water']
        milk_m -= MENU[order]['ingredients']['milk']
        coffee_m -= MENU[order]['ingredients']['coffee']
        payment -= MENU[order]['cost']
        print(f"Here is ${round(payment, 2)} dollars in change")
        return [MENU[order]['cost'], water_m, milk_m, coffee_m]
    else:
        print(f"Sorry that's not enough money. Money refunded: {payment}.")
        return [0, water_m, milk_m, coffee_m]


def money_count_user(penny, nickles, dimes, quarters):
    money_user = (penny*0.01) + (nickles*0.05) + (dimes*0.1) + (quarters*0.25)
    return round(money_user, 2)


while mechine_start:
    user_oder = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_oder.lower() == 'report':
        print(f"Water; {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\n money: $"
              f"{money}")
    elif user_oder == 'exit':
        mechine_start = False
    else:
        print(f"Total payment : {MENU[user_oder]['cost']}")
        if is_resource_sufficient(MENU[user_oder]['ingredients'], water, milk, coffee):
            user_penny = int(input("pennies: "))
            user_nickles = int(input("nickles: "))
            user_dimes = int(input("dimes: "))
            user_quarters = int(input("quarters: "))
            money_payment = money_count_user(penny=user_penny, nickles=user_nickles, dimes=user_dimes,
                                             quarters=user_quarters)
            print(f"Your money : {money_payment}")

            product = coffee_machine(order=user_oder, payment=money_payment,
                                     water_m=water, milk_m=milk, coffee_m=coffee)
            print(product)
            money += product[0]
            water = product[1]
            milk = product[2]
            coffee = product[3]
