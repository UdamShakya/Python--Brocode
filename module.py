import math
#print(help(math))

import numpy as np
from numpy import minimum #sometimes can create naming confusion 

minimum_value = minimum(4, 10)
print("Minimum value between 4 and 10 is:", minimum_value)


# variable scope 
# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local, Enclosing, Global, Built-in

def func1():
    #variables defined within a funciton is a local variable
    a=1
    print(a)

def func2():
    b=2
    print(b)

func1()
func2() 

def func3():
    x=5
    def func4():
        print(x)
    # since x is not defined in the local version we move onto the enclosed variables
    func4()

func3()

