# #list
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)

# #print(dir(fruits))

# fruits.append("orange")
# print(fruits)

# print(len(fruits))

# fruits.remove("apple")
# print(fruits)
# fruits.sort() #alphabetical order
# fruits.reverse() # reverse alphabetical order
# print(fruits)
# fruits.insert(0,"kiwi")
# print("pineapple" in fruits)

# print(fruits.index("banana"))
# print(fruits.count("kiwi")) # returns the count of "kiwi"

# #Sets (unordered and immutable)
# fruits_set = {"apple", "banana", "cherry"}
# print(fruits_set)

# print(dir(fruits_set))
# #print(help(fruits_set))

# fruits_set.add("orange")
# print(fruits_set)

# fruits_set.add("apple") # no effect, as sets do not allow duplicates
# fruits_set.add("kiwi")

# fruits_set.remove("banana")
# fruits_set.pop()

# print(fruits_set)

# #tuple
# fruits_tuple = ("apple", "banana", "cherry","coconut","coconut")
# print(fruits_tuple)

# print(dir(fruits_tuple))
# print(fruits.index("coconut"))

# print(fruits_tuple.count("coconut"))


# #Shopping cart program

# foods =[]
# prices =[]
# total = 0

# while True:
#     food= input("enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"enter the price of {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("----- Your cart------")

# for food in foods:
#     print(food, end=" ")

# for price in prices:
#     total += price

# print(f"\nTotal: ${total:.2f}")


# 2D Lists  

# fruits = ["apple","orange","banana", "kiwi"]
# vegetables = ["carrot","potato","onion","cabbage"]
# meats = ["chicken","beef","pork","lamb"]

# groceries = [fruits, vegetables, meats]
# print(groceries[1])
# print(groceries[0][2])
# sports = [["soccer", "basketball", "baseball"], 
#           ["tennis", "golf"],
#            ["hockey"]]

# for category in groceries:
#     for item in category:
#         print(item,end=" ")
#     print()

# # 2d tuple 
# # good for numpad as tuple is ordered and unchangeable 
# num_pad = (
#     (7, 8, 9),
#     (4, 5, 6),
#     (1, 2, 3),
#     ("*", 0, "#")
# )

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()


#Python quiz game 

questions = ("how many elements in the periodic table?: ",
             "what is the capital of France?: ",
             "who wrote 'Hamlet'?: ",
             "what is the largest planet in our solar system?: ",
             "what is the boiling point of water?: "
            )

options= (("a) 118", "b) 120", "c) 115", "d) 112"),
          ("a) Paris", "b) London", "c) Berlin", "d) Madrid"),
          ("a) Shakespeare", "b) Dickens", "c) Austen", "d) Twain"),
          ("a) Jupiter", "b) Saturn", "c) Earth", "d) Mars"),
          ("a) 100°C", "b) 90°C", "c) 80°C", "d) 70°C")
        )

answers = ("a", "a", "a", "a", "a")
guesses = []
score = 0
question_num=0

for i in range(len(questions)):
    print(questions[i])
    for option in options[i]:
        print(option)
    guess = input("Enter your answer (a, b, c, d): ").upper()
    guesses.append(guess)
    if guess == answers[i].upper():
        score += 1
        print("correct")
    else:
        print("wrong")
        print(f"The correct answer was: {answers[i].upper()}")

    question_num += 1
print("------------------")
print(f"Your final score is {score} out of {len(questions)}")
print("Score breakdown:")
for i in range(len(questions)):
    print(f"Question {i + 1}: {questions[i]}")
    print(f"Your answer: {guesses[i]}")
    print(f"Correct answer: {answers[i]}")
    print()