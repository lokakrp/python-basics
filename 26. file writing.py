# how to write a file

text = "Hey :p\nThis is my file\nHave a good day"    # \n is used to create a new line

#with open("test.txt","r")                           # used to read a file
with open("test.txt","w") as file                    # used to write a file
     file.write(text)

with open("test.txt","a") as file                    # used to append a file (add text to it)
     file.write(text)