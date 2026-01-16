
def birthday_song(name, age):
    print(f"happy birthday to you {name}")
    print(f"you are {age} years old")
    print("happy birthday to you")

birthday_song("John", 30)

birthday_song("Alice", 25) #arguments and parameters positions matter

def display_invoice(username,amount,due_date):
    print(f"Invoice for {username}")
    print(f"Amount Due: ${amount:,.2f}")
    print(f"Due Date: {due_date}")

display_invoice("johndoe", 1500.7545, "2024-07-15")


# return function

def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Division by zero error"
    
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))


def create_name(first,last):
    first= first.capitalize()
    last= last.capitalize()
    return first+ " "+ last

full_name = create_name("john", "doe")
print("Full Name:", full_name)  

#default arguments and keyword arguments
import time 
def clock(start, end=30):
    for i in range(start, end + 1):
        print("Current time:", i)
        time.sleep(1)

clock(25)  # uses default end value of 30

def hello(greeting,title,first,last):
    print(f"{greeting}, {title} {first} {last}!")

hello(greeting="Hello", title="Dr.", first="Jane", last="Smith")
hello("hello", title="Mr",last="perera",first="Supun")

print("hello", end= " ")

