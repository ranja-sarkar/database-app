#Working with files

f = open("input.txt","w")       #Creates a file. If already there, opens file

print (f.name)                  #Name of the file
print (f.mode)                  #Chosen operation mode
print (f.closed)                #Checks if file is closed and returns boolean

f.write("This is line one\n")
f.write("Mary had a little lamb\n")
f.write("Humpty-Dumpty sat on a wall\n")

f.close()                       #Closes the file
print (f.closed)
