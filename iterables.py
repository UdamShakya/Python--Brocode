
numbers =(1,2,3,4,5)

for number in reversed(numbers):
    print(number, end= "-")

fruit ={"apple","banana","cherry"}
for fruit in fruit:
    print() 
    print(fruit, end="")

print()
word = "Bro code"
for char in word:
    print(char, end=" ")

dictionary={"name":"John","age":30,"city":"New York"}

for key in dictionary.keys():
    print(key, end=" ")

for value in dictionary.values():
    print(value, end=" ")

for key,value in dictionary.items():
    print()
    print(f"{key}: {value}", end=" ")

# Membership operators

word = "apple"

letter = input("Enter a letter in the secret word: ")

if letter in word:
    print(f"{letter} is in the word!")
else:
    print(f"{letter} is not in the word.")

students ={"spongebob","patrick","sandy"} #sets,lists,tuples act the same

student = input("Enter student name: ")

if student.lower() in students:
    print(f"{student} is enrolled in the class.")
else:
    print(f"{student} is not enrolled in the class.")


#dictionary

grades = {"spongebob": 90, "patrick": 85, "sandy": 95}

student= input("Enter student name: ")

if student.lower() in grades:
    print(f"{student}'s grade is {grades[student.lower()]}.")
else:
    print(f"{student} is not found in the gradebook.")


email="udamilukpotha@gmail.com"

if "@" in email and "." in email:
    print("Valid email address.")
else:
    print("Invalid email address.")
