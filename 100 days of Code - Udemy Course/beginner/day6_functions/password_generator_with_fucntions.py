import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ========== FUNCTIONS ==========

def greetings():
    print("Welcome to the PyPassword Generator!")

def collect_inputs():

    num_letters = int(input("How many letters would you like in your password? "))
    num_symbols = int(input(f"How many symbols would you like? "))
    num_numbers = int(input(f"How many numbers would you like? "))

    return num_letters, num_symbols, num_numbers

def random_pick(char_list, num_letters, num_symbols, num_numbers):

    for i in range(num_letters):
        char_list.append(random.choice(letters))

    for i in range(num_symbols):
        char_list.append(random.choice(symbols))

    for i in range(num_numbers):
        char_list.append(random.choice(numbers))

    return char_list

def mix_characters(char_list):
    random.shuffle(char_list)

    return char_list

def create_password(char_list):
    password = "".join(char_list)

    return password

# ===============================

# ========== BODY ===============

greetings()

num_letters, num_symbols, num_numbers = collect_inputs()

char_list = list()

char_list = random_pick(char_list, num_letters, num_symbols, num_numbers)

char_list = mix_characters(char_list)

password = create_password(char_list)

print(f"Your Password is: {password}")

# ===============================