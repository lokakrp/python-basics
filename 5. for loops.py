# For loops - executes block of code a limited number of times


import time

#for i in range(10):                        # this will make it count to 10
#    print (i+1)                            # this will make it start from 1 instead of 0



for i in ("Loka"):                    # this will print out my name a letter at a time - prints each index
    print (i)

for i in range (10):                        # this will print out my name 10 times
   print ("Loka")

for num in range(0,10,1):                   # this will count from 1 to 10 -- start index is inclusive so 0 will print
  print (num + 1)



for num in range(10,0,-1):                  # this will count from 10 to 0 -- stop index is exclusive so 0 won't print     
   print (num)



for seconds in range(10,0,-1):
   print (seconds)
   time.sleep(1)                            # this will set a delay of 1 second to emulate counting down!
print("it has been 10 seconds!")             



greeting = "hello"                          # this will print hello 10 times
for i in range(10):
   print (greeting)