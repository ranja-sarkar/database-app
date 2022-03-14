#Searching in a text

text = "Mary had a little lamb"

print ("lamb" in text)              #searches for lamb in 'text' and returns boolean

print (text.endswith("lamb"))       #returns 'True' if 'text' ends with 'lamb'

print (text.startswith("lamb"))     #returns 'True' if 'text' starts with 'lamb'

print (text.endswith("Mary"))       #returns 'True' if 'text' ends with 'Mary'

print (text.startswith("Mary"))     #returns 'True' if 'text' starts with 'Mary'
