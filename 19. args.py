# *args = parameter that pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def add(num1,num2):
  sum = num1 + num2
  return sum

#print(add(1,2,3))                           # this will not work as there are 3 values, and only two are asked for in the add function


# same code using args
# * must be used, args is naming convertion but tuple can be named anything


def add(*args):                             # this will accept any arguments and collects them into a tuple named "args"
    sum = 0
    for i in args:
       sum += i                             # this will add all arguments of i to the sum
    return sum

print(add(1,2,4,8))

# tuples are created with *, meaning that values cannot be changed
# a way to counter this is through casting

def adding(*s):              
    sum = 0
    stuff = list(stuff)                     # casting to a list, as lists are changeable
    stuff[0] = 0                            # this would not work without casting
    for i in stuff:
       sum += i              
    return sum

print(adding(1,2,4,8))