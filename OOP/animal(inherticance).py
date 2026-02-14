#Inheritance = allows a class to inherit attributes and methods from another class
#helps with code reusability and extensibility
#class Child(Parent)

#mulitple inheritance - inhertifrom more than one parent class C(A,B)
#muultilevel inheritance - a class can be derived from another derived class

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

#multiple inheritance and multilevel inheritance 

class animal:
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")

class prey(animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class predator(animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class rabbit(prey):
    def __init__(self, name):
        self.name = name

class hawk(predator):
    def __init__(self, name):
        self.name = name
    pass

class fish(prey, predator):
    def __init__(self, name):
        self.name = name

rab= rabbit("Bunny")
fishie =fish("Nemo")

fishie.hunt()
fishie.flee()
rab.flee()

rab.eat()
rab.sleep()
fishie.eat()