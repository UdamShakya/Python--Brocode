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



# rock , paper , scissor 

options=("rock", "paper", "scissors")
player = None
computer= random.choice(options)
playing = True 

while playing:
    player = None
    computer= random.choice(options)
    while player not in options:
        player = input("Enter a choice (Rock, paper, scissors): ").lower()

    print(f"Computer chose: {computer}")
    print(f"Player chose: {player}")

    if player ==computer:
        print("It's a tie!")
    elif player== "rock" and computer== "scissors":
        print("Rock smashes scissors! You win!")
    elif player== "paper" and computer== "rock":
        print("Paper covers rock! You win!")
    elif player== "scissors" and computer== "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("You lose!")

     
    if input("Do you want to play again? (yes/no): ").lower() != "yes":
        playing = False
        print("Thanks for playing!")
