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


#python Calculator
operator= input("Enter an operator (+, -, *, /): ")
num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))

if operator== "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator== "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator== "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator== "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Division by zero error.")
else:
    print("Invalid operator.") 


#Python weight Converter

weight= float(input("enter your weight : "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    print(f"Your weight in pounds is: {weight * 2.20462}")
elif unit.upper() == "L":
    print(f"Your weight in kilograms is: {weight / 2.20462}")
else:
    print("Invalid unit.")

#temperature conversion

temp = float(input("Enter temperature: "))
unit = input("Is this in (C)elsius or (F)ahrenheit? ")

if unit.upper() == "C":
    print(f"Temperature in Fahrenheit is: {temp * 9/5 + 32}")
elif unit.upper() == "F":
    print(f"Temperature in Celsius is: {(temp - 32) * 5/9}")
else:
    print("Invalid unit.")
