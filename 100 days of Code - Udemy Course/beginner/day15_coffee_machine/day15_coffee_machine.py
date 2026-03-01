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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# ============ FUNCTIONS ============

def coffee_choice():
    while True:
        coffee_option = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_option.lower() == "espresso" or coffee_option.lower() == "latte" or coffee_option.lower() == "cappuccino":
            coffee_option = check_resources(coffee_option.lower())
            return coffee_option
        elif coffee_option.lower() == "off":
            return coffee_option
        elif coffee_option.lower() == "report":
            return coffee_option
        else:
            print("Invalid option, try again\n")

def check_resources(coffee_option):

    for ing, amount in MENU[coffee_option]["ingredients"].items():
        if resources[ing] < amount:
            print(f"Not enough {ing}!")
            return "Not enough"
    return coffee_option

def report():
    print(f"\nWater: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}\n")

def coin_insert(coffee_chosen):

    while True:

        try:
            print("Please insert coins.\n")
            quarter = int(input("How many quarters? "))
            dime = int(input("How many dimes? "))
            nickle = int(input("How many nickles? "))
            pennie = int(input("How many pennies? "))

            if quarter < 0 or dime < 0 or nickle < 0 or pennie < 0: raise ValueError

            break

        except ValueError:

            print("Invalid Option. Type a valid number\n")

    total = quarter * 0.25 + dime * 0.1 + nickle * 0.05 + pennie * 0.01

    result_of_the_checking = cost_check(coffee_chosen, total)

    if result_of_the_checking != "Not enough money":
        deduct_resources(coffee_chosen)

    return result_of_the_checking

def cost_check(coffee_chosen, total):

    if MENU[coffee_chosen]["cost"] < total:
        change = total - MENU[coffee_chosen]["cost"]
        print(f"That's your change: ${change:.2f}")
        resources["money"] += total - change
        return str(change)
    elif MENU[coffee_chosen]["cost"] == total:
        resources["money"] += total
        return "No changes"
    else:
        print("You have not inserted enough coins to this drink")
        return "Not enough money"

def deduct_resources(coffee_chosen):
    
    for ing, amount in MENU[coffee_chosen]["ingredients"].items():
        resources[ing] -= amount

# ===================================


# ============ BODY =================

while True:

    coffee = coffee_choice()

    if coffee == "off": break
    elif coffee == "report": report()
    elif coffee == "Not enough":
        print("Try another option\n")
        continue

    if coffee != "report":

        if coin_insert(coffee) == "Not enough money":
            print("Try again\n")
            continue

        print(f"Here is your {coffee}, enjoy it!")

# ===================================