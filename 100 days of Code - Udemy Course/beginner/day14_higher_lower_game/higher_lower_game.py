import art, game_data, random
# ====== FUNCTIONS =====
def greetings():
    print(art.logo)
    print("Welcome to the game Who Has More Followers!\n\n")

def choose_comparison(A_func, B_func, right_guess):

    if not right_guess: A_func = random.randint(0, len(game_data.data) - 1)
    else:
        A_func = B_func

    while True:

        B_func = random.randint(0, len(game_data.data) - 1)

        if A_func != B_func: break

    return A_func, B_func

def comparison(A_func, B_func):
    print("A: " + game_data.data[A_func]['name'] + ", " + game_data.data[A_func]['description'] + " from " + game_data.data[A_func]['country'])

    print(art.vs)

    print("B: " + game_data.data[B_func]['name'] + ", " + game_data.data[B_func]['description'] + " from " + game_data.data[B_func]['country'])

def user_guess(A_func, B_func):

    while True:
        guess_func = input("\nWho Has more followers? Type 'A' or 'B': ")
        if guess_func.upper() == 'A':
            guess_func = A_func
            break
        elif guess_func.upper() == 'B':
            guess_func = B_func
            break
        else:
            print("Invalid option. Try again!\n")

    return guess_func

def answer(A_func, B_func):
    most_followed_func = []

    if game_data.data[A_func]['follower_count'] > game_data.data[B_func]['follower_count']:
        most_followed_func = game_data.data[A_func]

    elif game_data.data[B_func]['follower_count'] > game_data.data[A_func]['follower_count']:
        most_followed_func = game_data.data[B_func]

    return most_followed_func

# ======================

# ===== BODY =====
greetings()

score = 0
right_guess = False

A = []
B = []

while True:

    A, B = choose_comparison(A, B, right_guess)

    comparison(A, B)

    guess = user_guess(A, B)

    most_followed = answer(A, B)

    if most_followed == game_data.data[guess]:
        score += 1
        print(f"You're Right! Current Score: {score}\n\n")
        right_guess = True
    else:
        print(f"That's Wrong. Final Score: {score}")
        break

# ======================