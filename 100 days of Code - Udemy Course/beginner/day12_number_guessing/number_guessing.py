import art
import random

def greetings():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")

def select_difficulty():

    while True:
        difficulty_func = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()

        if difficulty_func != "easy" and difficulty_func != "hard":
            print("Wrong option. Try Again\n")
        else:
            break

    return difficulty_func

def select_number():
    number_func = random.randint(1, 100)

    return number_func

def define_attempts(difficulty_func):

    attempts_func = 0

    if difficulty_func == "easy":
            attempts_func = 10
    elif difficulty_func == "hard":
            attempts_func = 5

    return attempts_func

def check_guessing(guess_func, number_func):

    if guess_func > number_func:
        return "Too high!"
    elif guess_func < number_func:
        return "Too low!"
    else:
        return "That's correct!"

def check_result(number_func, attempts_func):
    if attempts_func == 0:
        print("\nYou lost all your tries!")
        print(f"The number was {number_func}")

    else:
        print("\nYou win!")

greetings()

difficulty = select_difficulty()

attempts = define_attempts(difficulty)

number = select_number()

print("I'm thinking of a number between 1 and 100.")

while attempts > 0:

    print("\n\n")

    while True:

        try:
            guess = int(input("Guess a number: "))
            if guess not in range(1, 101): print("Invalid number. Try Again\n")
            else: break
        except ValueError:
            print("Please type a valid integer.\n")

    checking_match = check_guessing(guess, number)

    print(checking_match)

    if checking_match == "That's correct!": break

    attempts -= 1
    print(f"{attempts} attempts left!")

check_result(number, attempts)