#list
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

#Sets (unordered and immutable)
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set)

print(dir(fruits_set))
#print(help(fruits_set))

fruits_set.add("orange")
print(fruits_set)

fruits_set.add("apple") # no effect, as sets do not allow duplicates
fruits_set.add("kiwi")

fruits_set.remove("banana")
fruits_set.pop()

print(fruits_set)

#tuple
fruits_tuple = ("apple", "banana", "cherry","coconut","coconut")
print(fruits_tuple)

print(dir(fruits_tuple))
print(fruits.index("coconut"))

print(fruits_tuple.count("coconut"))


#Shopping cart program

foods =[]
prices =[]
total = 0

while True:
    food= input("enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- Your cart------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"\nTotal: ${total:.2f}")
