# how to read files

try:                                     # try is used with code that MAY cause an exception, so it does error handling
  with open("test.txt") as file:         # there's no file.txt in my directory so this won't run!
   print(file.read())
except FileNotFoundError:
  print("That file was not found :(")