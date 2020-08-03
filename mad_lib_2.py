# Starting with an empty dictionary
madlib_word_choices = {
"noun": {},
"verb": {},
"adjective": {}
}

#User is prompted for inputs and these inputs are stored to the dictionary
#John was drinking a cold beer when his parrot attacked
madlib_word_choices["noun"][0] = input("Enter a noun: ") #John
madlib_word_choices["verb"][0] = input("Enter a verb: ") #drinking
madlib_word_choices["adjective"][0] = input("Enter an adjective: ") #cold
madlib_word_choices["noun"][1] = input("Enter a noun: ") #beer
madlib_word_choices["noun"][2] = input("Enter a noun: ") #parrot
#String interpolation prints the different inputs to the sentence
print("%s was %s a %s %s when his %s attacked." % (madlib_word_choices['noun'][0], madlib_word_choices['verb'][0], madlib_word_choices['adjective'][0], madlib_word_choices['noun'][1], madlib_word_choices['noun'][2])) 

#New set of user inputs that are stored in the dictionary
# e.x: He dropped his beer and chased the parrot into the wrong alley.
madlib_word_choices["verb"][1] = input("Enter a verb: ") #Dropped
madlib_word_choices["noun"][3] = input("Enter a noun: ") # Beer
madlib_word_choices["verb"][2] = input("Enter a verb: ") #Chased
madlib_word_choices["noun"][4] = input("Enter a noun: ") # Parrot
madlib_word_choices["adjective"][1] = input("Enter an adjective: ") #Wrong
madlib_word_choices["noun"][5] = input("Enter a noun: ") #Alley
#string interpolation to use the inputs in the sentence
print("He %s his %s and %s the %s into the %s %s." % (madlib_word_choices['verb'][1], madlib_word_choices['noun'][3], madlib_word_choices['verb'][2], madlib_word_choices['noun'][4], madlib_word_choices['adjective'][1], madlib_word_choices['noun'][5])) 

