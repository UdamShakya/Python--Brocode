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