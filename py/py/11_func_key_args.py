#Keyword - arguments

def wish(name,age):
    print("Hello {} you are {} year old".format(name,age))

wish("India",67)
wish(67,'India')

wish(age = 67, name = 'India')

#When calling a function using keyword arguments, the order of arguments doesn't
#matter
