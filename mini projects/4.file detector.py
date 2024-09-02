# discovering a file!!! 

import os 

path = ""
dir = ""
dir_path = ""

print("welcome to file discovery!!")
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
print(path)

if os.path.isfile(path):
  print ("this file exists")
else:
  print("this file does not exist")

