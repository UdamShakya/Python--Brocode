#Inheritance = allows a class to inherit attributes and methods from another class
#helps with code reusability and extensibility
#class Child(Parent)

class animal:
    def __init__ (self,name):
        self.name=name
        self.is_alive =True


    def eat(self):
        print(f"{self.name} is eating.")    

    def sleep(self):
        print(f"{self.name} is sleeping.")

class  Dog(animal):
    def bark(self):
        print(f"{self.name} is barking.")

class cat (animal):
    def meow(self):
        print(f"{self.name} is meowing.")

class mouse(animal):
    def squeak(self):
        print(f"{self.name} is squeaking.")

dog = Dog("Buddy")
cat = cat("Whiskers")
mouse = mouse("Jerry")

print(dog.name)
dog.eat()
