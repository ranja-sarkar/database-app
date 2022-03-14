#Files Assignment 1

f = open ("input1.txt","r")          #open file
for line in f:
    words = line.split(" ")     #split with space
    print (words[0])
f.close()
#append them into a list
#get first and last words


f = open ("input1.txt",'r')          #open file
for line in f:
    print (line.rstrip().split(" ")[-1])
f.close()
