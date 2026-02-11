print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? (10 12 15): "))

while True:
    people = int(input("How many people to split the bill? "))

    if people <= 0:
        print("\nThere must be at least one person, try again!")
    else:
        break

result = (bill / people) * (1 + (tip / 100))

print(f"It'll be ${result:.2f} for each")
