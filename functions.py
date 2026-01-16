
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