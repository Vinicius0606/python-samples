print("Welcome to Python Pizza Deliveries!")

while True:
    size = input("What size pizza do you want? S, M or L: ").upper()
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
    extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

    if size not in ('S', 'M', 'L'):
        print("\nWrong type of size, try again")
    elif pepperoni not in ('Y', 'N'):
        print("\nWrong input for pepperoni, try again")
    elif extra_cheese not in ('Y', 'N'):
        print("\nWrong input for extra_cheese, try again")
    else:
        break

bill = 0

if size == 'S':
    bill += 15
    pepperoni_cost = 2

elif size == 'M':
    bill += 20
    pepperoni_cost = 3

elif size == 'L':
    bill += 25
    pepperoni_cost = 3

if pepperoni == 'Y':
    bill += pepperoni_cost

if extra_cheese == 'Y':
    bill += 1


print (f"Your final bill is: ${bill}.")
