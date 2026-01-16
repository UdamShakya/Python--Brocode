import random
#print(help(random))

number=random.randint(1, 10)

low=1 
high=100

num= random.randint(low, high)
num2= random.random()

options =("rock", "paper", "scissors")
Cards =["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
option= random.choice(options)
random.shuffle(Cards)

print(Cards)

print(num2)

print("Random number between 1 and 10:", number)


