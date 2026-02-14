# super() function

class shape:
    def __init__ (self,colour,filled):
        self.colour=colour
        self.filled=filled 

    def describe(self):
        print(f"it is {self.colour} and {'filled' if self.filled else 'not filled'} ")



class circle(shape):
    def __init__ (self,colour,filled,radius):
        super().__init__(colour,filled)
        self.radius=radius

    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14*self.radius*self.radius}cm² and a radius of {self.radius}cm")

class square(shape):
    def __init__ (self,colour,filled,length):
        super().__init__(colour,filled)
        self.length=length

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.length*self.length}cm² and a length of {self.length}cm")

    

class triangle(shape):
    def __init__ (self,colour,filled,base,height):
        super().__init__(colour,filled)
        self.base=base
        self.height=height
    

circle = circle("red",True,5)
square = square("blue",False,4)

print(circle.colour)
print(circle.filled)
print(f"circle radius: {circle.radius}cm")

circle.describe()