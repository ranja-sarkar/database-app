#Function Assignment


def diff(a,b):
    if a > b:
        return a-b
    else:
        return b-a



def diff1(x,y):
    if y > x:
        x,y = y,x
    return x-y

print (diff(3,9))
print (diff1(6,1))
