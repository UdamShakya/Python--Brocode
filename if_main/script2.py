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

def get_payout(row, bet ):
    if row[0] == row[1] == row[2]:
        if row[0] == "⭐️":
            return bet * 10
        elif row[0] == "🔔":
            return bet * 5
        elif row[0] == "🍋":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 1  
        elif row[0] == "🍒":
            return bet * 10
        else:
            return 0
    return 0

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
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won {payout:,.2f}!")
            balance += payout
        else:
            print("Sorry, you didn't win this time.")

        play_again = input("Do you want to play again? (y/n): ").lower()

        if play_again != "y":
            break

    print("Game over! Your final balance is:", balance)

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
