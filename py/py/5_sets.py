#Sets
""" A set is an unordered list of distinct elements """
a = (2,4.5,6,7,4,5,6,3,6,7,4,7,7,4,87,8,6)
print (a)
aSet = set(a)                                   #Converting a list into set
print (aSet)
print (type(aSet))                              #Prints datatype of 'aSet'

b = (2,4,6,3,5,6,3,56,7,8)
print (b)
bSet = set(b)
print (bSet)

c = aSet - bSet                                 #Deletes common elements and returns remainder

mybuddies = {"rita", "vicky", "sita", "saketh"}
print (mybuddies)
mysisbuddies = {"sita", "gita", "rita", "bata"}
print (mysisbuddies)

print (mybuddies.union(mysisbuddies))           #Prints all friends' names of me and my sister
print (mybuddies.intersection(mysisbuddies))    #Prints friends' names common to us
print (mybuddies - mysisbuddies)                #Prints friends' names exclusive to me
