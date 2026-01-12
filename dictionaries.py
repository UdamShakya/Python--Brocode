
Capitals  = {"usa": "Washington D.C.", "france": "Paris", "japan": "Tokyo","china": "Beijing"}

print(Capitals)
print(dir(Capitals))
print(Capitals["france"])
#print(help(Capitals))

if Capitals.get("usa"):
    print("The capital of USA is", Capitals["usa"])
else:
    print("that capital doesn't exist")

# Capitals.update({"germany": "Berlin"})
# Capitals.pop("china")
# Capitals.popitem()
# Capitals.clear()

print(Capitals)
keys = Capitals.keys()

for key in keys:
    print(key)

values = Capitals.values()

for value in values:
    print(value)

items = Capitals.items()

for key, value in items:
    print(key, value)


#Concession Stand Program 

concession_stand = {
    "hotdog": 5.00,
    "popcorn": 3.50,
    "soda": 2.00,
    "candy": 1.50
}

cart = []
total=0
print("Welcome to the Concession Stand!")
for key, value in concession_stand.items():
    print(f"{key:10}: ${value:.2f}")

print("----------------------------")

while True:
    item = input("Enter the item you want to buy (or 'done' to finish): ")
    if item == "done":
        break
    if item in concession_stand:
        cart.append(item)
        total += concession_stand[item]
    else:
        print("Item not found.")

print("Your cart:")
for item in cart:
    print(f" - {item}: ${concession_stand[item]:.2f}")

print(f"Total: ${total:.2f}")