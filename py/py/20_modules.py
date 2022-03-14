#modules

import time                             #Importing time module

starttime = time.time()                 #assigning 'time' function from 'time'

for x in range(10000):                  #x varies from 0 to 10000
    y = x**x                            #evaluates x^x
endtime = time.time()                   #gives operation end time

print (endtime - starttime)             #gives total time of the operation

time.sleep(1)                           #program sleeps for a second

from datetime import datetime

d= datetime.now()

print (d.year)
print (d.month)
print (d.second)

c=datetime.today()
print (c)
