from script1 import *

def favourite_drink(drink):
    print("My favourite drink is", drink)

def main():
    print("this is script2")
    favourite_drink("coffee")
    favourite_food("pizza")
    print("goodbye")

if __name__ == "__main__":
    main()
