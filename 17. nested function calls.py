# nested function calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for next outer function

# TWO METHODS FOR SAME EXACT SAME THING

# first method:

num = input("Enter a whole positive number: ")         
num = float(num)
num = abs(num)
num = round(num)
print(num)


# second method

print(round(abs(float(input("Enter a whole positive number: ")))))