# from script1 import *
import random 

# def favourite_drink(drink):
#     print("My favourite drink is", drink)

# def main():
#     print("this is script2")
#     favourite_drink("coffee")
#     favourite_food("pizza")
#     print("goodbye")

# if __name__ == "__main__":
#     main()


#Python slot machine

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐️"]

    return [random.choice(symbols) for _ in range(3)]
     

def print_row(row):
    print(" | ".join(row))

def get_payout():
    pass

def main():

    balance = 100
    print("******************")
    print("Welcome to the slot machine!")
    print(" 🍒 🍉 🍋 🔔 ⭐️" )
    print("******************")

    while balance>0 :
        print(f"Your balance is {balance:,.2f}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("You cannot bet more than your current balance.")
            continue

        if bet <=0:
            print("Bet amount must be greater than zero.")
            continue

        balance -= bet

        row = spin_row()
        print_row(row)
        get_payout()

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
