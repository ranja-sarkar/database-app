#Assignment1

strlist = ["rajesh", 'ramesh', 'raghav', 'raman', 'ravi', 'ali', 'sara']
print (strlist)                             #String list
strlist.sort()                              #Sorts the list in Alphabetical
print (strlist)
print (strlist[-4:])                        #Prints the last four elements


numlist = [1, 2.0, 3.16, 5.67, 8, 10]       #Numbers list
print (numlist)
numlist.remove(min(numlist))                #Removing the least element in list
print (numlist)
print (9 in numlist)                        #Returns a boolean value for the
                                                #condition
