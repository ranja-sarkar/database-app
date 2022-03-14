#Loops

if 3 > 1:
    print ("True")                  #Indentation is very important in Python
else:
    print ("False")

count = 0
while count < 11:
    print (count)
    count+= 1
print ("End of while loop")

for a in range(5):
    print (a, "You've got it")

for x in range(2,5):
    print (x, x*x)                  #runs for x value from 2 till 5

for x in range(1,10,2):             #valid for x value from 1 till 10 in steps of 2
    print (x)
for x in range(90,80,-1):           #backward count from 90 till 80
    print (x)

colours = ["red", 'blue', 'green', 'white', 'black']

for color in colours:
    print (color)

for index, color in enumerate(colours):
    print (index+1, color)          #counts the number of iterations done
