#file ops

f = open("C:\\Users\\ravi\\Desktop\\Mongo Factory Docs\\Synechron\\input1.txt","r")
                                    #opens specified file in the path
for line in f:
    print (line)                    #prints 
    print (line.rstrip())
    print (line,end="")

f.close()
