MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_enough_resources(drink_ingredients):
    """Verify that there are enough ingredients for the requested drink"""
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Ups, sorry. There is not enough {ingredient}")
            return False
    return True

def ask_for_coins():
    """Ask for the money that the drink costs"""
    print("Please insert coins: ")
    total = int(input("How many quarters (0.25c)?: ")) * 0.25
    total += int(input("How many dimes (0.10c)?: ")) * 0.1
    total += int(input("How many nickles (0.05c)?: ")) * 0.05
    total += int(input("How many pennies (0.001c)?: ")) *0.01
    return total

def print_report():
    """Prints the actual resources and profit in the machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit}")

def all_successful(payment,drink_cost):
    """Validate if everything is ok to continue"""
    if payment >= drink_cost:
        change = payment - drink_cost
        print(f"Here is your change: {change}. Thanks for being a coffee yunki")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Payment is not enough. Money refunded.")
        return False

def make_coffee(choice, drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] = resources[ingredient] - drink_ingredients[ingredient]
    print(f"Here do you have your: {choice}")
    return True

is_on = True

while is_on:
    choice = input("What would you like? [espresso/latte/cappuccino]: ")
    """ To power-off the machine. Not shown in the previous prompt because it is for admins """
    if choice == "off":
        is_on = False
    elif choice == "report":
        print_report()
    else:
        drink = MENU[choice]
        if is_enough_resources(drink["ingredients"]):
            payment = ask_for_coins()
            if all_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
