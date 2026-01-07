#If statements - most basic form of decision making in Python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")

if age>=18:
    print("You are eligible to vote.")
elif age<0:
    print("Invalid age.")
else:
    print("You are a minor. You are not eligible to vote.")


Response = input("would you like some food? (Y/N): " )

if Response=="Y":
    print("Here is your food.")
else:
    print("Okay, maybe next time.")


name =input("Enter your name: ")

if name=="":
    print("Name cannot be empty.")
else:
    print(f"Hello, {name}!")

for_sale =True
if for_sale:
    print("The item is for sale.")
else:
    print("The item is not for sale.")