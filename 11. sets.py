# sets - collection that is unordered, unindexed and has no duplicate values

utensils = {"fork", "spoon", "knife", "comically large spoon"}
dishes = {"plate", "bowl", "cup", "comically large spoon"}


# ---- useful methods!!

utensils.add("spork")                          #  adds spork to set
# utensils.remove("fork")                      #  removes fork from set
# utensils.clear()                             #  clears entire set
# utensils.update(dishes)                      #  adds dishes set to utensils set
dinner_table = utensils.union(dishes)          #  combines sets into a new set

print(utensils.difference(dishes))             #  finds out what utensils has that dishes doesn't
print(dishes.difference(utensils))             #  finds out what dishes has that utensils doesn't

print(utensils.intersection(dishes))           #  finds out what utensils has that dishes also has
print(dishes.intersection(utensils))           #  finds out what dishes has that utensils also has


# --- printing the set

for x in dinner_table:
  print(x)                                                                                    # this will print each index in no particular order
       


# ---- example of no duplicates

cutlery = {"fork", "spoon", "knife", "knife", "knife", "knife","knife"}

for x in cutlery:                                                                             # no duplicate values - knife will appear once
  print(x)






































# sets practice


anime = {"nichijou", "danshi koukousei no nichijou", "gintama" "regular show"}
shows = {"the office", "parks and recs", "breaking bad", "regular show"}

print(anime.difference(shows))
print(anime.intersection(shows))
anime.add("azumanga daioh")
shows.clear()
TV = anime.union(shows)
anime.update(shows)


for x in anime:
  print (x)


