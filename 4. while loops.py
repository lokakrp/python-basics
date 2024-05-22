# while loops - execute block of code while condition specific is met

# x = 1
#
# while x == 1:
#    name = input ("what is your name: ")

name = ""

while len(name) == 0:
   name = input("please enter your name: ")


# loop to ask for age

age = int(input("what is your age: "))

while age <= 0:
  print("please enter a valid age")
  age = int(input("what is your age: "))


# loop for creating password

password = input("please enter a password: ")

while len(password) < 5:
   print("password must be greater than 5 characters")
   password = input("please enter a password: ")


# loop for creating password IMPROVED

while True:                                                                                              # creates loop for whole input
   password = input("please enter a password: ")
   
   if len(password) < 5 and not any(char.isupper() for char in password):                                # checks if password is less than 5 characters
      print("password must contain uppercases and be greater than 5 characters")

   elif len(password) < 5:                                                                               # checks if password is less than 5 characters
      print("password must be greater than 5 characters")

   elif not any(char.isupper() for char in password):                                                    # checks if password contains capital letters
      print("password must contain uppercases")

   else:
      print("password is valid")
      break                                                                                              # stops the loop - place inside loop to stop loop input from breaking
