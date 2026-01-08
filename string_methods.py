name = input("Enter your name: ")
result = len(name)
print(result)

Result =name.find("u")
Resultt=name.rfind("q")
print(Result)
print(Resultt)

name = name.upper()
name = name.lower()
name = name.capitalize()
print(name)

test = name.isdigit()
test= name.isalpha()
print(test)

phone_number = input("Enter your phone number: ")
phone_number.count("-")
phone_number=phone_number.replace("-"," ")
print(phone_number)


#Exercise 1 validate user input exercise
username= input("Enter username: ")

if len(username) > 12:
    print("Username must be under 12 characters.")
elif not username.find(" ") == -1:
    print("Username must not contain spaces.")
elif not username.isalpha():
    print("Username must only contain letters.")
else:
    print(f"Welcome, {username}!")


#String Indexing

credit_number= "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:5]) #Starting index is included ending index is not included
print(credit_number[5:])
print(credit_number[-1])

last_digits= credit_number[-4:]

print(f"**** **** **** {last_digits}")
reverse= credit_number[::-1]
print(reverse)

#format specifiers


