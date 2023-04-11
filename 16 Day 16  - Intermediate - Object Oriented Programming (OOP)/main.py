from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

while coffe_maker.power:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    """ To power-off the machine. Not shown in the previous prompt because it is for admins """
    if choice == "off":
        coffe_maker.power_off()
    elif choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)