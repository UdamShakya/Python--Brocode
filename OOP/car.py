#object - A Bundle of related attributes and methods
#Class - blueprint used to design the structure and the layout of an object

class car:
    def __init__(self,model,year,colour,for_sale):
        self.model=model
        self.year=year
        self.colour=colour
        self.for_sale=for_sale

    def drive(self):
        print(f"The car is driving {self.model}")

    def stop(self):
        print(f"The car has stopped {self.model}")
 
 #class variable = shared among all instances of a class 
 #Defined outside the constructor 
 #allow you to share data among all objects created from that class

class student:
    class_year = 2004
    Num_student = 0


    def __init__(self,name,age):
        self.age=age
        self.name=name
        student.Num_student += 1


        




