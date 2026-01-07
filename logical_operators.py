temp = 25 
is_raining = False

if temp > 30 and not is_raining:
    print("It's a hot and sunny day!")
elif temp > 30 and is_raining:
    print("It's a hot day, but it's raining.")
elif temp <= 30 and not is_raining:
    print("The weather is nice and pleasant.")
else:
    print("It's a cool and rainy day.")


if temp > 20 or is_raining:
    print("The weather is either warm or it's raining.")


#conditional statements
num = 5 
a=6
b=7
age = 13 
temperature = 30 
user_role= "admin"


weather = "hot"if temperature > 25 else "cold"
print (weather)

max_num = a if a > b else b
min_num = a if a < b else b
status = "adult" if age >= 18 else "minor"

access = "full access" if user_role.lower() == "admin" else "limited access"


