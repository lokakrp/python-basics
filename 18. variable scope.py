# scope = region that variable is recognised
#         variable is only available within region of creation
#         global and locally scoped versions of a variable can be created


name = "lokanatha"             # global scope variable - available within and outside functions


def display_name():
  name="lok"                   # local scope variable - only available within function
  print(name)                  # local variable is prioritised here


print(name)                    # will not print name from within the function
display_name()                 # this will print name from within function



##   LEGB ORDER RULES

# L = Local
# E = Enclosing
# G = Global
# B = Built-in