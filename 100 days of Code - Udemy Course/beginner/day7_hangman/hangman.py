import random
from hangman_art import stages, logo
from hangman_words import word_list

word = random.choice(word_list)

placeholder = ""

for letter in word:
    placeholder += "_"

game_over = False

correct_letters = []
guessed_letters = []

tries = 6

print(logo)

print(placeholder + "\n")

while not game_over:

    display = ""

    while True:

        guess = input("Guess a letter: ")
        if guess in guessed_letters:
            print("You've already tried that word, try again.")
        else:
            break

    guessed_letters.append(guess)

    for letter in word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in correct_letters:
        tries -= 1

        print(stages[tries])

        if tries <= 0:
            print(f"You lost! the word was {word}")
            game_over = True

    if "_" not in display:
        print(f"You win with {tries} tries left!")
        game_over = True

    
    print(f"You have {tries} tries left!\n")