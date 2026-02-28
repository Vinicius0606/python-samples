import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):

    if n2 != 0:
        return n1 / n2
    else:
        print("Cannot divide by 0")
        return "Try Again"

print(art.logo)

calc_operations = {"+":add, "-":subtract, "*":multiply, "/":divide}

print("Welcome to the calculator program!")

n1 = int(input("Please input the first number: "))

while True:
    n2 = int(input("Please input the second number: "))

    operator = input("Please choose an operator(+, -, *, /): ")

    result = calc_operations[operator](n1, n2)

    if result == "Try Again": continue

    print(f"{n1} {operator} {n2} = {result:.2f}")

    choice = input("Wanna keep using the last result? (yes or no): ")

    if choice.lower() == "yes":
        n1 = result

    elif choice.lower() == "no":
        n1 = int(input("Please input the first number: "))

    else:
        break