# loop control statements  = change a loops execution from its normal sequence

# break =      used to terminate the loop
# continue =   skips to next iteration of loop     
# pass =       act as placeholder, does nothing


# FOLLOWING LOOP WILL BREAK WHEN A NAME IS ENTERED PROPERLY, OTHERWISE WILL LOOP

while True:
  name = input("please enter your name: ")
  if name != "":                                   # if nothing is entered, it will loop
    break                                          # loop will break if something else is entered

# FOLLOWING LOOP WILL PRINT THE PHONE NUMBER WITH NO DASHES

phone_number = "123-456-7890"

for i in phone_number:                       
  if i == "-":                                      # checks if current character is -
    continue                                        # skips past the -, checks each other character of phone number
  print(i, end="")                                  # end="" prevents new line       print statements by default will add a new line


  # FOLLOWING LOOP WILL SKIP PAST 13 BECAUSE IM SCARED OF THAT NUMBER

  for i in range(1,21):

    if i == 13:                                 
      pass
    else: 
      print(i)