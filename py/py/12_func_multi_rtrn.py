#Function that returns multiple values

"""Python functions can return any number of values"""

def sumdiff(a,b):
    return a+b,abs(a-b)
print (type(sumdiff(4,9)))
mysum, mydiff = sumdiff(4,9)
print (mysum, mydiff)
