import os

# checks if location exists (it does)

path = "C:\\picture of cat\\meow.jpg"

if os.path.exists(path):
  print("that location exists ", end="")
  if os.path.isfile(path):
    print("and it is a file")
  elif os.path.isdir(path):
    print("and it is a directory")
else:
  print("That location does not exist")


# discovering a file!!! (practice)

path = ""
dir = ""
dir_path = ""

drive = input("please enter the letter of your drive: ")
drive = drive + ":\\"

while True:
  option = input("search for file or directory? ").lower()
  if option == "directory":
    dir_name = input("please enter directory name: ").lower()
    dir_path = f"{dir_name}\\{dir_name}"
  else:
    break         
if option == "file":
  if dir_path != "":
    file = "\\" + input("enter name of exact name of file:")
  else:
    file = input("enter name of exact name of file:")


path = drive + dir_path + file

if os.path.isfile(path):
  print ("this file exists")
else:
  print("this file does not exist")
