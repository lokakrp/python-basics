# exception - events detected udring execution that interrupt flow of programs

# in this calculator, division by zero will cause exception

try:
  numerator = int(input("enter number to divide: "))
  denominator = int(input("enter number to divide by: "))
  result = numerator / denominator

# this code will handle the exception errors

except ValueError:                                         # removes the error for division by string
  print("Enter numbers only plz")

except ZeroDivisionError as e:                             # prints the error for division by 0
  print(e)
  print("you can't divide by zero!!! idiot!!!")

except Exception:                                          # basic exception handle which solves no problems
  print("Something went wrong")

else:
    print(result)                                          # value returned if no errors
finally:                                                   
  print("This will always execute!")                       # always executes regardless