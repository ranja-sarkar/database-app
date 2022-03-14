#!/usr/bin/Python 3
#1.py written by Ravi P. Teja
#String manipulation

name = "A quick brown fox jumps over a lazy dog."            #Declare a string

print (len(name))
                                            #Prints length of the given string
print (type(name))
                                            #Prints the data type of the 'name'

print ("The first letter of the given string is ",name[0])
                                            #Prints element that's located at index 0 i.e., the first element
print (name[-1])                            #Prints element that's located at index -1 i.e., the last element
print (name[0:5])                           #Prints elements from index 0 till index 5
print (name[5:10])                          #Prints elements from index 5 till index 10

print (name.upper())                        #Prints the entire string in uppercase
print (name.lower())                        #Prints the entire string in lowercase
print (name.capitalize())                   #Prints the first letter in uppercase and remaining all in lowercase
print (name.swapcase())                     #Prints the entire string in reversed typecases
print (name.title())                        #Prints every starting letter of a word in Capital


print (name[0:10:2])                        #Prints every second letter from index 0 to index 10
print (name[::1])                           #Prints every first letter in a string from beginning to end i.e., the complete string
print (name[::-1])                          #Prints every first letter in the string backwards
