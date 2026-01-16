import random
#print(help(random))

# number=random.randint(1, 10)

# low=1 
# high=100

# num= random.randint(low, high)
# num2= random.random()

# options =("rock", "paper", "scissors")
# Cards =["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# option= random.choice(options)
# random.shuffle(Cards)

# print(Cards)

# print(num2)

# print("Random number between 1 and 10:", number)

#python number guessing game 

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses =0
is_running= True

print("python number guessing game ")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")
    if not guess.isdigit():
        print("Invalid input. Please enter a number.")
        continue

    guess = int(guess)
    guesses += 1

    if guess < lowest_num or guess > highest_num:
        print(f"Please select a number between {lowest_num} and {highest_num}.")
    elif guess == answer:
        print(f"Congratulations! You've guessed the number {answer} in {guesses} attempts.")
        is_running = False
    elif guess < answer:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


