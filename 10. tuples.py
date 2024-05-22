# tuples = collection that is ordered and cannot be changed
#          used to group together related date

student= ("Ryan", 17, "male")

print(student.count("Ryan"))                                                  # print how many times "ryan" occurs
print(student.index("male"))                                                  # prints the index that "male" is in


# tuple tricks :3

for x in student:                                                             # this will print the values within the tuple
  print (x)

if "Ryan" in student:                                                         # checks if ryan is within student
  print("Ryan is here")                 