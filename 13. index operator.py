# index operator [] - gives access to a sequence's elements (str, list, tuples)



# name input that ensures cases of name are correct

name = input("What is your name: ")

if(name[0].islower()):                      # checks to see if first character is lower case
  name = name.capitalize()                  # capitalises first letter of name

if name[1:].isupper():                      # checks if rest of name from second character is upper case
  name = name[0]+name[1:].lower()           # makes rest of name lowercase - starts from second character ends

print("Hello " + name)



# random testing

uppername = name[:].upper()                                                # makes name uppercase
lowername = name[:].lower()                                                # makes name lowercase
last_character = name[-1]                                                  # last character of name
slast_character = name[-2]                                                 # second last character of name

print ("your uppercase name is " + uppername)
print ("your lowercase name is " + lowername)
print ("last character of name is " + last_character)
print ("second last character of name is " + slast_character)
