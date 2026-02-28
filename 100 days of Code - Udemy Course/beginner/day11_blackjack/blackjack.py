import random
import art

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)

def ace_checking(cards):
    while 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1

    return cards

def calculate_score(cards):

    cards = ace_checking(cards)

    return sum(cards)

def compare_result(u_score, c_score):
    if (u_score > 21 and c_score > 21) or u_score == c_score:
        print("It's a draw")

    elif u_score > 21 or (u_score < c_score and c_score <= 21):
        print("Computer wins!")

    elif c_score > 21 or (c_score < u_score and u_score <= 21):
        print("You win!")

while True:

    flag = input("Wanna play blackjack? (y or n): ")

    print("\n" * 16)

    if flag.lower() != "y":
        break

    print(art.logo)

    user_cards, com_cards = [], []

    for _ in range(2):
        user_cards.append(deal_cards())
        com_cards.append(deal_cards())

    print(f"Your hand: {user_cards}\nComputer hand: ?, {com_cards[1]}")

    user_score = calculate_score(user_cards)
    com_score = calculate_score(com_cards)

    while True and user_score < 21:

        while True:

            choice = input("\nKeep hand or draw one more card? (k or d): ").lower()

            if choice != "k" and choice != "d": print("Invalid option. Try Again\n")
            else: break

        if choice == "k": break

        user_cards.append(deal_cards())

        user_score = calculate_score(user_cards)

        print(f"\nYour current hand: {user_cards} = {user_score}\n")

        if user_score >= 21: break

    while com_score < 17:
        com_cards.append(deal_cards())

        com_score = calculate_score(com_cards)

    print(f"Your final hand: {user_cards} = {user_score}\nComputer final hand: {com_cards} = {com_score}")

    compare_result(user_score, com_score)