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

