# print(dir())
# from script2 import *


# def main():
#     favourite_food("Pizza")
#     print("this is script1")

# def favourite_food(food):
#     print("My favourite food is", food)


# #python banking program 

# def  show_balance(balance):
#     print(f'Your balance is {balance:,.2f}')

# def deposit(balance):
#     amount=float(input("Enter amount to deposit: "))
    
#     if amount< 0:
#          print("Invalid amount. Please enter a positive value.")
#     else:
#          return amount

# def withdraw(balance):
#     amount = float(input("Enter amount to withdraw: "))
#     if amount < 0:
#         print("Invalid amount. Please enter a positive value.")
#     elif amount > balance:
#         print("Insufficient funds.")
#     else:
#         return amount

# def main():
#     balance = 0
#     is_running = True

#     while is_running:
#         print("-----Banking program-----")
#         print("1. Show Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             show_balance(balance)
#         elif choice == "2":
#             balance += deposit(balance)
#         elif choice == "3":
#             balance -= withdraw(balance)
#         elif choice == "4":
#             is_running = False
#         else:
#                 print("Invalid choice. Please try again.")

#     print("Thank you for using the banking program.")

# if __name__ == "__main__":
#     main()


# Encryption program

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

# Encrypt
# print(f"chars: {chars}")
# print(f"keys: {keys}")

plain_text= input("Enter text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"Plain text: {plain_text}")
print(f"Cipher text: {cipher_text}")

#decrypt
cipher_text= input("Enter text to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"Cipher text: {cipher_text}")
print(f"Plain text: {plain_text}")
