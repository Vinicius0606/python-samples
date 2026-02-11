print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

while True:

    choice = input("\nYou're at a cross road. Where do you want to go?\n\tType 'left' or 'right': ").lower()

    if choice != "left":
        print("\nYou fell into a hole. Game Over.")
    else:
        choice = input("\nYou're at a cross road. Where do you want to go?\n\t"
                      + "Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()

        if choice != "wait":
            print("\nYou get attacked by an angry trout. Game Over.")
        else:
            choice = input("\nYou arrive at the island unharmed. There is a house with 3 doors.\n\t"
                          + "One red, one yellow and one blue. Which colour do you choose: ")

            if choice == "red":
                print("\nIt's a room full of fire. Game Over.")

            elif choice == "blue":
                print("\nYou enter a room of beasts. Game Over.")

            elif choice == "yellow":
                print("\nYou found the treasure! You Win!")

            else:
                print("\nYou died from mis-typeness. Game Over.")

    while True:
        choice = input("Wanna play again? (y/n): ").lower()

        if choice == 'y' or choice == 'n': break
        else: print("Invalid option, try again.\n")

    if choice == "n": break