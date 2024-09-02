# roll the dice!!!

import random

sides = [1,2,3,4,5,6]
accanswers = ["yes", "no"]

# function for rolling a dice

def diceroll():
  return random.choice(sides)

# function to ask to roll dice

def rollthedice():
  result = 0
  play = ""

  while play != "no":
    play = input("would you like to roll? ").lower()
    if play == "yes":
      result = diceroll()
      print(f"you rolled a {result}!")
    elif play == "no":
      print("ok why are u here???")
    elif play not in accanswers:
      print("invalid option")
      return play
    
# function to repeat process 


def repeat():
  playagain = input("would you like to try again? ").lower()
  if playagain == "yes":
      rollthedice()
  elif playagain == "no":
     print("ok bye")
  else:
        print("Invalid option")

 # code to start and repeat the game

play = rollthedice()
if play != "no":
   repeat()
