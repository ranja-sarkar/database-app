#Formatting

text = "      good morning   \t"

print ( "---------->{}<-----------".format(text))           #placeholder

print ( "---------->{}<-----------".format(text.lstrip()))  #removes left whitespaces

print ( "---------->{}<-----------".format(text.rstrip()))  #removes right whitespaces

print ( "---------->{}<-----------".format(text.strip()))   #removes whitespaces at
                                                            #at start and end
