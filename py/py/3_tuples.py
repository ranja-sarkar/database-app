#tuples

a = (2,4,7,3,8,0,5)                 #Tuple declaration

#Operations on tuple

print ( type(a) )                   #Prints datatype of 'a'
print (a[0])                        #Prints element in index 0
print (a[-1])                       #Prints element in index -1
print (len(a))                      #Prints length of the tuple
print (sum(a))                      #Prints the sum of elements in tuple
print (min(a))                      #Prints the least element in tuple
print (max(a))                      #Prints the highest element in tuple
print (a[2:5])                      #Prints elements from index 2 till index 5
print (a[::2])                      #Prints every second element from the start to the end of tuple
print (a[-4:-1])                    #Prints elements from index -4 till index -1

#Fuctions that can be used in tuples

b = 3,5,6,7                         #Alternate declaration of tuple
print (type(b))
print (b.count(3))                  #Counts number of times '3' present
print (b.index(5))                  #Locates the position of '5'
print (b[2])                        #Prints the element in index 2
