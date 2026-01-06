
#variables 
#strings 
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

#user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))
is_student = input("Are you a student? (True/False): ")

print(f"hello {name}")  

#Exercise 1 Rectangular Area Calc

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