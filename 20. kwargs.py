# **kwargs = paramater that packs all arguments into a dictionary
#            useful so that a function accepts a varying amount of keyword arguments

def hello(first, last):
  print("hello " + first + " " + last)

# hello(first="Ryan", middle="Lok", last="Kapoor")                 # there will be an error due to unexpected argument
# below is an example of kwargs being used

def hi(**kwargs):                                                   
  print("hello " + kwargs['first'] + " " + kwargs['last'])         # this code will work but is inefficient - must retain order of "first" being first
                        

hi(first="Ryan", middle="Lok", last="Kapoor")


# ** must be used, "kwargs" is a naming convention but any name can be used for dictionary
#bellow

def hey(**names):                                                   
  print("hello", end=" ")                                         # end=" " prevents new line from being made
  for key,value in names.items():                                 # goes through indexes of the dictionary
    print (value,end=" ")      

hey(title="Mr.", first="Ryan", middle="Lok", last="Kapoor")       # can hold any order of keys 