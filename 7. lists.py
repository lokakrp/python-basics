# lists - used to store multiple values in a single variable



drink = ["milk", "water", "apple juice", "orange juice", "pepsi", "coke", "sprite", "dr pepper", "green tea"]

print (drink)                                                                   # prints entire list
print (drink[0])                                                                # prints first item in list
print (drink[3])                                                                # prints 4th item in list

for x in drink:
  print(x)                                                                      # prints individual elements in list

drink.append("coffee")                                                          # adds coffee to the list                  
print(drink[9])                                                                 # prints newly added drink

drink.remove("apple juice")                                                     # removes apple juice because its nasty!!!  

drink.pop()                                                                     # this gets rid of the last item in the list - green tea
drink.insert(2, "green tea")                                                    # this inserts green tea in third,  because green tea is great and should be near first!

drink.sort()                                                                    # this will sort the list alphabetically

drink.clear()                                                                   # this removes all elements from the list


# task for lists

menu = ["pizza", "chicken", "sandwich", "steak", "pasta", "salmon", "ketchup"]

# fat guy - "HEY I WANT TO SEE THE MENU"

for x in menu:
  print(x)

# owner - "HEY WHY IS KETCHUP ON THIS MENU!!! GET RID OF IT!!!"

menu.pop

# fat guy - "HEY YOU GUYS DON'T HAVE XL PIZZAS??? ADD THIS IMMEDIATELY"

menu.append("XL pizza")

# fat guy - "PUT IT TO THE FRONT OF THE MENU NOW!!!!"

menu.remove("XL pizza")
menu.insert(0, "XL pizza")

# fat guy - ok i don't like this food, get rid of this menu now

menu.clear()

# fat guy - "ok u guys are out of business now bye"