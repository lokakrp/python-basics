# Basic 'if' statement
x = 10
if x > 5:
    print("x is greater than 5")

# 'if else' statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# 'if elif else' statement
z = 8
if z > 10:
    print("z is greater than 10")
elif z == 8:
    print("z is equal to 8")
else:
    print("z is less than 10 and not equal to 8")

# Multiple conditions with 'and'
a = 7
b = 12
if a > 5 and b > 10:
    print("Both a is greater than 5 and b is greater than 10")

# Multiple conditions with 'or'
c = 4
d = 9
if c > 5 or d > 5:
    print("Either c is greater than 5 or d is greater than 5")

# Nested 'if' statements
e = 15
if e > 10:
    print("e is greater than 10")
    if e > 20:
        print("e is also greater than 20")
    else:
        print("e is not greater than 20")

# Checking if a value is in a list
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list of fruits")

# Using 'not' to reverse the condition
is_raining = False
if not is_raining:
    print("It is not raining, let's go for a walk!")

