#Dictionary
"""
Dictionary contains elements in form of pairs seperated by a ':'
enclosed in curly braces {} as {key1:value1, key2:value2, ..}
"""
d = {'H':'Hydrogen', 'O':'Oxygen'}          #Dictionary syntax
print (type(d))
print (len(d))
print (d.keys())                            #Prints all keys
print (d.values())                          #Prints all values
print (d.items())                           #Prints all pairs of keys & values
print (d['H'])                              #Prints value of key 'H'
print (d.get('H'))                          #Meaningful way of above expression
d['C'] = 'Carbon'                           #Adding a value with key 'C'
print (d)
print (len(d))                              #Number of pairs
del d['H']                                  #Removing key 'H' and it's value
print (d)
