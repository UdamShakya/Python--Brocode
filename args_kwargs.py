
# * unpacking operator is important not the name of the arg
def add (*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1,2,3,4))


def name (*names):
    for name in names:
        print(name,end=" ")

name("udam","shakya","ilukpotha")


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Main St", city="Anytown", state="CA", zip="12345")

 
