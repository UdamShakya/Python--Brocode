doubles =[]

# for x in range(1,11):
#     doubles.append(x*2)

# print(doubles)

doubles = [x*2 for x in range(1, 11)]
print(doubles)

triples= [y*3 for y in range(1,10)]
print(triples)

squares=[z**2 for z in range(1, 11)]
print(squares)


fruits = ["apple","orange","banana","grape"]

fruits = [fruit.upper() for fruit in fruits]

fruit_char=[fruit[0] for fruit in fruits    ]

print(fruits)
print(fruit_char)

numbers = [1,-2,3,-4,5,6,-7]

positive=[num for num in numbers if num > 0]
negative=[num for num in numbers if num < 0]
even=[num for num in numbers if num %2 == 0]
print(positive)
print(negative)
print(even)

grade =[84,34,123,223,95,90,31]

passing=[score for score in grade if score >= 60]

print(passing)