#Magic methods = Dunder methods __init__,__str__,__eq__
#they are automatically called by many of python's built in operations.
#they allow developers to define or customize the behaviour of objects


class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"

    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title and
                    self.author == other.author and
                    self.pages == other.pages)
        return False
    
    def __lt__(self, other):
        if isinstance(other, Book):
            return self.pages < other.pages
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Book):
            return self.pages > other.pages
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Book):
            return f"{self.pages + other.pages} pages"
        return NotImplemented

    def __getkey__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            print(self.author)  
        elif key == "pages":
            return self.pages
        return NotImplemented
    



book1=Book("The Great Gatsby","F. Scott Fitzgerald",180)
book2=Book("Harry Potter","J.K. Rowling",320)
book3=Book("Harry Potter","J.K. Rowling",320)

print(book1)
print(book2)
print(book3)

print(book2 == book3)  
print(book1+book2)
print(book1 < book2)
print(book1 > book2)

# book1['author']


#@property = Decorator used to define a method as a property

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:1f}cm"

    @property
    def height(self):
        return f"{self._height:1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            print("Width must be positive")
        self._width = new_width

    @height.setter
    def height(self, new_height):
        if new_height <= 0:
            print("Height must be positive")
        self._height = new_height

    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    

rectangle =Rectangle(5,10)

rectangle.width =6

print(rectangle.width)



#decorators = A function that extends the behaviour of another function

def add_sprinkles(func):
        def wrapper(*args, **kwargs):
            print("Adding sprinkles")
            func(*args, **kwargs)
        return wrapper

@add_sprinkles
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream!")

get_ice_cream("chocolate")