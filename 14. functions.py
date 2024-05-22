# function = block of code that is executed only when called        -        useful for code that is often repeated, helps to save time
 
# first

def hello():                                            # def = define function
    print("hello!")

hello()                                                 # function will execute code written under defined function

# second

def meeting(name):
    print("hello " + name)

meeting("ryan")

# third

def greet(name):
    print("hello "+ name)
my_name = "Gurtrude"

greet(my_name)                                             # this will still greet gurtrude          

# fourth

def greeting(first_name, last_name):
    print("hello " + first_name + " "+ last_name) 

greeting("Ryan", "Kapoor")                                 # places both values into the variables

# fifth

def hey(firstname, secondname, age):
    print ("hello " + firstname +" " + secondname + " you are " + str(age) + " years old")
    print("Have a nice day!")
hey("Ryan","Kapoor",17)