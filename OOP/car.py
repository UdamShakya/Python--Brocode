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




