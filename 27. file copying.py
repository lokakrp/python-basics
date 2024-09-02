# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil                                                                # module used for file creation/modification

shutil.copyfile("test.txt","C:\\users\\loka\\Desktop\\copy.text")            # two arguments: source and destination
