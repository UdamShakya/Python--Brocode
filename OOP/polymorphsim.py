from abc import ABC,abstractmethod


class shape(ABC):

     @abstractmethod
     def area(self):
         pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class square(shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Pizza(circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

    

shapes = [circle(5), square(4), triangle(3, 6), Pizza("pepperoni", 10)]

for shape in shapes:
    print(f"Area: {shape.area()}cm²")

#Duck typing 
#Abject must have minimum necessary attributes/methods 

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Car:
    alive = False
    def speak(self):
        return "Beep beep!"

animals = [Dog(), Cat(),Car()]

for animal in animals:
    print(f"Animal alive: {animal.alive}")
    print(animal.speak())
