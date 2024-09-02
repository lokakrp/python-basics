import os                                             # module for file and directory functions
import shutil                                         # module for advanced file operations - such as deleting branches

# For files
path = "test.txt"                                     # establishes a file path
#os.remove(path)                                      # removes specified path

try:
  os.remove(path)                                     # Try to remove the file at the specified path
except FileNotFoundError:
  print("That file was not found")                    # Print a message if the file does not exist
except PermissionError:
  print("You do not have permission to delete that")  # Print a message if permission is denied
else:
  print(path + " was deleted successfully")           # Print a success message if file deletion is successful

# For folders
path = "folder"                                       # establishes a folder path 
#os.rmdir(path)                                       # removes specified path only if empty

try:                                                  # try is for testing for exception
  os.rmdir(path)                                      
  #shutil.rmtree(path)                                # removes a folder and its contents
except FileNotFoundError:                             # checks if folder doesn't exist 
  print("That file was not found")                    
except PermissionError:                               # checks if permissions are denied for the folder
  print("You do not have permission to delete that") 
except OSError:                                       # checks if folder is not empty and cannot be deleted with rmdir
  print("You cannot delete that with that function")  
else:
  print(path + " was deleted successfully")           
