
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