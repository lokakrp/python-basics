import os                                           # OS module is for interacting with the operating system and for file operations.

# this can also be used for the moving of folders by changing source + destination to a filder
# i.e - source = "folder"

source = "test.txt"                                 # path of the file

destination = "test\\lol.txt"                       # path of where to move to, also able to rename the file

try:
    if os.path.exists(destination):                 # checks if a file already exists there
        print("There is already a file there")  
    else:
        os.replace(source, destination)             # Moves/renames the source file to the destination, if already exists it will be replaced
        print(source + " was moved")  
except FileNotFoundError:                           # handles the exception in case file doesn't exist
    print(source + " was not found")          
