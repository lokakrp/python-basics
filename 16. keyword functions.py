# keyword arguments = arguments preceded by identifer when passed to a function
#                     order of arguments dosen't matter, unlike positional arguments
#                     python knows names of arguments that function receives

def hello(first, middle, last):
  print("Hello " +first+" "+middle+" "+last)


hello("Ryan", "Lok", "Kapoor")                           # position of arguments matter here
hello(last="Kapoor", first="Ryan", middle="Lok")         # position doesn't matter as specified