
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

