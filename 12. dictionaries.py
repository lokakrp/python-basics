# dictionary - changeable, unordered, collection of unique key: values pairs
#              fast because they use hashing
#              allows access to value quickly


# Creation of Dictionary  -   Key:Value

capitals = {'USA':"Washington DC",                      # use '' for key and "" for value 
            'India':"New Delhi",
            'Japan': "Tokyo",                             
            'China': "Beijin",
            'Russian': "Moscow"}          



# useful methods for dictionaries :p

print(capitals['India'])                                # uses key, not index
print(capitals.get('Germany'))                          # checks if key exists - prevents breaking code
print(capitals.keys())                                  # prints the keys
print(capitals.values())                                # prints the values
print(capitals.items())                                 # prints entire dictionary, list form        

for key,value in capitals.items():
  print (key,value)                                     # prints entire dictionary


# useful methods for dictonaries pt 2!!!!!!!

capitals.update({'Germany':"Berlin"})                   # this will add key:value as Germany:Berlin
capitals.update({'India':"Peshawar"})                   # updated the capital of india - india has invaded pakistan and peshawar has been labelled the new capital!!!!
capitals.pop('China')                                   # removes key:value of China because DEATH TO COMMUNISTS!!!!
capitals.clear()                                        # clears entire capitals dictionary


