#modules random

import random

print (random.randint(3,100))                       #random integers from 3 and 100


folks = ["mary","pradeep","vineet","raj","ravi"]

random.shuffle(folks)                               #shuffles within the list (indices change)

print (random.choice(folks))
