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


#class methods = Allow operations related to class itself


class Student:
    count=0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.gpa += gpa

    @classmethod
    def get_student_count(cls):
        return cls.count
    
    #instance method
    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.gpa / cls.count:.2f}"


student1 = Student("Alice", 3.5)
student2 = Student("Bob", 3.8)
student3 = Student("Charlie", 3.2)

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())

print("Total Students:", Student.get_student_count())
print("Average GPA:", Student.get_average_gpa())