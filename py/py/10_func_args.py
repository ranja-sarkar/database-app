#Functions with arguments with default values
"""Functions take arguments from right side. Default values must be assigned
from right side."""
def add(x,y=10):
    return x+y                  #Try to use a single return in a function

c = add(4,5)
d = add(5)
print (c,d)
print (add(5,6),add(8))