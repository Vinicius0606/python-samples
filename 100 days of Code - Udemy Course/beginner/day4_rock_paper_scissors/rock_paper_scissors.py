import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    player_choice = int(input("What would like to play:\n1 - Rock\n2 - Paper\n3 - Scissor\n"))
    if player_choice not in (1, 2, 3):
        print("Invalid option, type a valid number\n")
    else:
        break

playable_choices = [rock, paper, scissors]
cpu_choice = random.randint(0, 2)

print(f"Computer plays: {playable_choices[cpu_choice]}")

if cpu_choice == 0:

    if player_choice == 1:
        print("It's a draw")
    elif player_choice == 2:
        print("You win!")
    else:
        print("You lost!")

elif cpu_choice == 1:

    if player_choice == 1:
        print("You lost!")
    elif player_choice == 2:
        print("It's a draw")
    else:
        print("You win!")

elif cpu_choice == 2:

    if player_choice == 1:
        print("You win!")
    elif player_choice == 2:
        print("You lost!")
    else:
        print("It's a draw")