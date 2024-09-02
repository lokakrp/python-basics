import random 

while True:
  choices = ["rock", "paper", "scissors"]

  computer = random.choice(choices)                               # establishes choice for computer
  player = None                                                   # establishes choice for player - none because you'll choose later

  while player not in choices:                                    # ensures that the right thing in the list is chosen
    player = input("rock, paper, or scissors?: ").lower()         # asks for input and .lower() prevents case sensitivity

  if player == computer:
      print("computer: ", computer)
      print("player: ", player)
      print("Tie!")
  elif player == "rock":
    if computer =="paper":
      print("computer: ", computer)
      print("player: ", player)
      print("Player loses!")   
    if computer =="scissors":
      print("computer: ", computer)
      print("player: ", player)
      print("Player wins!")
  elif player == "paper":
    if computer =="scissors":
      print("computer: ", computer)
      print("player: ", player)
      print("Player loses!")   
    if computer =="rock":
      print("computer: ", computer)
      print("player: ", player)
      print("Player wins!")
  elif player == "scissors":
    if computer =="rock":
      print("computer: ", computer)
      print("player: ", player)
      print("Player loses!")   
    if computer =="paper":
      print("computer: ", computer)
      print("player: ", player)
      print("Player wins!")       
 
  play_again = input("Play again? (yes/no): ").lower()

  if play_again !="yes":
    break                                                               # breaks out of the loop if answer doesn't equal yes

print("Thank you for playing")


  