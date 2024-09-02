# string slicing = creates a substring by extracting elements from another string
# two operators:    indexing [] or slice ()
# needs three indexes:  [start:stop:step]
# index starts at 0
# stop index does not include where you are stopping in the code
# leaving start blank = 0 , leaving stop blank = max value
# step will step characters a certain amount, similar to starts i.e step 2 will move 2 characters to the right

name = "David Beckham"

first_name = name[:4]                  # ends at first name
last_name = name[5:]                   # starts with last name
funky_name = name[::2]                 # skips a character
funky_first_name = name[:4:2]          # ends at first names, skips a character
funky_last_name = name[5::2]           # start at last name, skips a character
reversed_name = name[::-1]             # step will count backwards
reversed_first_name = name[3::-1]
reversed_last_name = name[:4:-1]


print ("your first name is " + first_name)
print ("your last name is " + last_name)
print ("no clue why, but your funky name is " + funky_name)
print ("also no clue why, but your funky name is " + funky_first_name)
print ("again no clue why, but your funky last name is " + funky_last_name)
print ("your name backwards is " +reversed_name)
print ("your first name backwards is " +reversed_first_name)
print ("your last name backwards is " +reversed_last_name)


# slice will start at 1
# second value will ask for negative index within slicing

google = "https://google.com"
wikipedia = "https://wikipedia.com"

slice = slice(8,-4)          # can be constantly reused for URLs

print(google[slice])
print(wikipedia[slice])

