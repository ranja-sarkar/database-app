#String splitting and joining

text = "val John, 24601, jeanvaljohn@lesmiserables.com"

print (text.split(","))             #prints the fields separated by ',' into a list

name, eid, email = text.split(",")  #assigns fields to respective variables

print (name, eid, email)            #prints respective variables

strings = ["hello", "how", "are", "you"]    #list named 'strings'

print (".".join(strings))           #joins elements with '.'

print (" ".join(strings))           #joins elements with ' '

print ("".join(strings))            #joins elements with null ""
