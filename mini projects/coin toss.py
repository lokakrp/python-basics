# coin toss
import random

face = ["heads","tails"]

def cointoss():
    play = "yes"
    while play == "yes":
        toss = ""
        while toss not in face:
            toss = input("heads or tails? ").lower()
            if toss not in face:
                print("invalid option, try again!")
        result = random.choice(face)
        if toss == result:
            print(f"you won! it landed on {result}")
        else:
            print(f"you lost, it landed on {result} :(")
        print (f"it landed on {result}!")
        play = input("play again? yes or no: ").lower()
        if play == "yes":
            cointoss()
        else:
            print("okay bye!!")

cointoss()