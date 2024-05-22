# random module usages
import random

x = random.randint(1,6)       # makes x random number between 1 and 6
print(x)
y= random.random()            # makes y random number between 0 and 1
print(y)


mylist = ["rock", "paper", "scissors"]
z = random.choice(mylist)
print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)