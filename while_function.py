name = input("Enter your name: ")

if name== "":
    print("You didn't enter a name.")
else:
    print(f"Hello, {name}!")


while name == "":
    print("Name cannot be empty. Please enter your name.")
    name = input("Enter your name: ")

print(f"Welcome, {name}!")

age = int(input("Enter your age: "))

while age < 0:
    print("Invalid age. Age must be positive.")
    age = int(input("Enter your age: "))

print(f"Your age is {age}.")

food= input("Enter the food you want: (press q to quit)").upper()

while not food== "Q":
    print(f"Here is your {food}.")
    food= input("Enter the food you want: (press q to quit)").upper()

print(f"Goodbye!")

num =int(input("Enter a number between 1 - 10 "))
while num < 1 or num > 10:
    print("Invalid number. Please try again.")
    num = int(input("Enter a number between 1 - 10 "))
print(f"You entered: {num}")


#python compound interest calcualtor

princple = 0
rate =0
time =0 

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount must be positive.")

while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Rate of interest must be positive.")

while time <= 0:
    time = float(input("Enter the time (in years): "))
    if time <= 0:
        print("Time must be positive.")

total= principal * pow(1 + rate / 100, time)
compound_interest = total - principal
print(f"The compound interest is: {compound_interest}")