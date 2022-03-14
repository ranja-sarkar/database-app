#!/usr/bin/Python 3
#2.py written by Ravi P. Teja
#lists

a = [2,4,7,3,8,0,5]                 #Created a list
print ( type(a) )                   #Prints datatype of 'a'
print (a[0])                        #Prints element in index 0
print (a[-1])                       #Prints element in index -1 (last one)
print (len(a))                      #Prints length of the list (No. of elements)
print (sum(a))                      #Prints sum of all elements
print (min(a))                      #Prints the minimum (least) element
print (max(a))                      #Prints the maximum (highest) element
print (a[2:5])                      #Prints elements from index 2 till index 5
print (a[::2])                      #Prints every second element in the list from start to end
print (a[-4:-1])                    #Prints elements from index -4 till index -1

a.append(10)                        #Adds an element '10' to the list as last element
print (a)
a.insert(1,100)                     #Adds an element '100' at index 1
print (a.index(0))                  #Prints he element at index 1
print (a)
print (a.count(4))                  #Prints the count of element 4 present in the list
a.sort()                            #Sorts the list in Ascending order
print (a)
a.reverse()                         #Reverses the order of the list
print (a)

print (a)
a.remove(7)                         #Removes element '7'
print (a)
c = a.pop()                         #Removes every element in the list
print (c)                           #Returns zero
print (a)
a.extend([7,8,9])                   #Adds elements 7,8,9 to the list
print (a)
