# THIS WILL NOT WORK AS I HAVE RENAMED THE MODULE TO 30.MESSAGESMODULE.PY

# module - files containing python code. contains functions, classes, etc.
# used with modular programming, which seperates a program into parts

import messagesmodule as msg           # imports the module i have created
                                       # "as msg" makes an alias for the module     

msg.bye()
msg.hello()

from messagesmodule import hello,bye

bye()                                 # runs the function created within the module
hello()

#help("modules")                        this will print out the official modules, but generally just check pythons documentation