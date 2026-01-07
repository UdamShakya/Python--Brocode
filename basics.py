
# #variables 
# #strings 
first_name = "bro"
food = "pizza"
print(f"hello {first_name}")
print(f"you like {food}")

#integers 
age = 25
print(f"you are {age} years old")
quantity = 3
print(f"you have ordered {quantity} {food}s")

#float

price = 10.99
gpa = 3.2
print(f"the price is ${price}")
print(f"your GPA is {gpa}")

#boolean

is_student = True
is_active = False
print(f"Are you a student? {is_student}")
print(f"Are you active? {is_active}")   

if is_student:
    print("Welcome, student!")  
else:
    print("Hello, guest!")


#Typecasting 

name = "udam"
age=25
gpa=3.5
is_student= True

gpa = int(gpa)
print(gpa)

age=str(age)
age += "1"
print(age)

name = bool(name)
print(name)

# user input
# Exercise 1 Rectangular Area Calc

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
print(f"The area of the rectangle is: {area}cm²")

#Exercise 2 Shopping cart Program 
item = input("Enter the item you want to purchase: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity you want to purchase: "))

total = price * quantity
print(f"You have purchased {quantity} {item}(s) for a total of ${total}.")


#madlibs game 

adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
adjective2 = input("Enter another adjective: ")
verb1 = input("Enter a verb: ")
adjective3 = input("Enter one more adjective: ")

print(f"Today I went ot a {adjective1} zoo.")
print(f"In an exhibit , I saw a {noun1}")
print (f"It was {adjective2} and {verb1}ing.")
print(f"I was {adjective3}!")

# Arithmetic Operators 
friends = 5
friends = friends + 1
friends += 1 #augmented operator 

friends -= 2
friends *= 3
friends **= 3
Remainder = friends % 3
print(friends)

x=3.14
y=4
z=5

Result = round(x)
Result= abs(y)
Result = pow(z,2)
Result= max(x,y,z)
Result= min(x,y,z)

print(Result)