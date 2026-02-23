# static methods = A method that belong to a class rather than any object from that class(instance)

#instance methods = Best for operations on instances of the class 
#static methods = Best for utility functions that don't need access to instance data

class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Developer", "Designer", "Intern"]
        return position in valid_positions
    

print(Employee.is_valid_position("Developer"))  
employee1 = Employee("Alice", "Developer")
employee2 = Employee("Bob", "Manager")
employee3 = Employee("Charlie", "Designer")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
