#File I/O - common scenarios

#Read file contents at once
f = open('input.txt', 'r')
print (f.read())
f.close()

#Read file char by char
f = open('input.txt', 'r')
print (f.read(1))
print (f.read(1))
f.close()

#Read file line by line
f = open('input.txt','r')
print (f.readline())
print (f.readline())
f.close()

#Read all lines into a list
f = open('input.txt', 'r')
lines = f.readlines()
print(lines)
f.close()

#Write into a new file
f = open('input.txt','w')
f.write("Et tu, Brutus?")
f.close()

#Append to an existing file
f = open('input.txt','a')
f.write("\nThis is a new line")
f.close()
