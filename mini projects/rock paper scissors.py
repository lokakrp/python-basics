import random

# rock paper scissors! 

def jankenpon():
  print("Welcome to Rock Paper Scissors - You will be against NANO!!")
  userhand = input("Rock, Paper, Scissors, SHOOT: ").lower()

  jankenpon = ["rock", "paper", "scissors"]
  hand = random.choice(jankenpon)

  #while userhand != "rock" and userhand != "paper" and userhand != "scissors":      # THIS WAS THE ORIGINAL
  while userhand not in jankenpon:                                                   # this is a better way, but i didn't get it from memory :(
    if userhand == "rockcispaper":
      print("THAT'S CHEATING,", end=" ")
    print("invalid option!!")
    userhand = input("Rock, Paper, Scissors, SHOOT: ").lower()

  while userhand == hand:
    print("you drew!!")
    hand = random.choice(jankenpon)
    userhand = input("Rock, Paper, Scissors, SHOOT: ").lower()

  if userhand == "rock" and hand == "scissors":
    print("NANO chose scissors - you won!!")
  elif userhand == "rock" and hand == "paper":
    print("NANO chose paper - you lost :(")
  elif userhand == "paper" and hand == "rock":
    print ("NANO chose rock - you won!!")
  elif userhand == "paper" and hand == "scissors":
    print ("NANO chose scissors - you lost :(")
  elif userhand == "scissors" and hand == "paper":
    print ("NANO chose paper - you won!!")
  elif userhand == "scissors" and hand == "rock":
    print ("NANO chose rock - you lost :(")
  else:
    print("wat")
    
jankenpon()

# loop for playing 

play = True

def loop():
  play = True
  while play == True:
    play = input("Play again? yes or no: ").lower()
    if play == "yes":
      jankenpon()
      loop()
loop()
print("Bye! It was nice playing with you :D")

  