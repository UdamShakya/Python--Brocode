#lists
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

#print(dir(fruits))

fruits.append("orange")
print(fruits)

print(len(fruits))

fruits.remove("apple")
print(fruits)
fruits.sort() #alphabetical order
fruits.reverse() # reverse alphabetical order
print(fruits)
fruits.insert(0,"kiwi")
print("pineapple" in fruits)

print(fruits.index("banana"))
print(fruits.count("kiwi")) # returns the count of "kiwi"

