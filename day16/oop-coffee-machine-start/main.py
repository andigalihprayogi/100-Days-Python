from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffeMaker = CoffeeMaker()
money = MoneyMachine()
menu_item = MenuItem
menu = Menu()

mechine_on = True

while mechine_on :
    user_want = input(f"What would you like? ({menu.get_items()}):").lower()
    if user_want == "report":
        coffeMaker.report()
        money.report()
    elif user_want == "off":
        mechine_on = False
    else:
        item = menu.find_drink(user_want)
        if coffeMaker.is_resource_sufficient(item):
            if money.make_payment(float(item.cost)):
                coffeMaker.make_coffee(item)
        else:
            mechine_on = False