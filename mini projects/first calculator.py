# first calculator attempt!

num_1 = int(input("please enter a number: "))
num_2 = int(input("please enter another number: "))



operation = int(input("please enter your operation: 1. Addition, 2. Multiplication, 3. Subtraction, 4. Division: "))

# loop to ask for operation

while operation < 1 or operation > 4:
  print("please enter valid option")
  operation = int(input("please enter your number for operation: 1. Addition, 2. Multiplication, 3. Subtraction, 4. Division: "))


# operation selection

if operation == 1:
  print (num_1 + num_2)
elif operation == 2:
  print (num_1 * num_2)
elif operation == 3:
  print (num_1 - num_2)
elif operation == 4:
  if num_2 == 0:
     print("division by 0 is not allowed")
  else:
    print (num_1 / num_2)
else:
  print("invalid operation!")


# seems like everything is working okay!!!!!!!!!!!!!