
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