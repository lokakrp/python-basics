# str.format() - method that gives users more control with displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)                                              # this is the original way to write a sentence
print("the {} jumped over the {}".format(animal, item))                                    # second method       - formatted items must be ordered
print("the {1} jumped over the {0}".format(animal, item))                                  # positional argument -  follows the index numbers of items within format()
print("the {food} jumped over the {name}".format(food="rice",name="ryan"))                 # variable can be assigned here, must include variables in {} 

text = "The {} jumped over the {}"               
print(text.format(animal,item))                                                            # formats seperately within print statement

# padding 

name = "ryan"

print("hello my name is {:10}. nice to meet you!".format(name))                   # adds padding of 10 - defaults to right
print("hello my name is {:<10}. nice to meet you!".format(name))                  # adds [addomg pf 10 to the right
print("hello my name is {:>10}. nice to meet you!".format(name))                  # adds padding of 10 to the left
print("hello my name is {:^10}. nice to meet you!".format(name))                  # centre aligns value (5 left and 5 right)


# cool tricks

pi = 3.14159
number = 1000

print("The number pi is {:.2f}".format(pi))                # f represents decimals, meaning 2 decimal places
print("The number is {:,}".format(number))                 # adds commas for 1000 places
print("The number is {:b}".format(number))                 # number represented in binary
print("The number is {:o}".format(number))                 # number represented in octals
print("The number is {:x}".format(number))                 # number represented in hexadecimal
print("The number is {:e}".format(number))                 # number represented in scientific notations 