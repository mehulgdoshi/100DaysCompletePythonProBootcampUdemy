from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_item = MenuItem()
menu = Menu()
is_on = True

def print_report():
    """Prints the report"""
    coffee_maker.report()
    money_machine.report()

while is_on:
    menu_items = menu.get_items()
    choice = input(f"What would you like? ({menu_items}]): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
