import random 

# list of answers

affirmative = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As i see it, yes", "Most likely", "Yes", "Outlook good", "Signs point to yes"]
noncommitive = ["Reply hazy, try again", "Ask again later", "Better not tell you now","Cannot predict no", "Concentrate and ask again"]
negative = ["Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
answers = [affirmative, noncommitive, negative]

# program for Magic 8 ball

x = 0                                                                  # start of loop
print("type 'break' at any point to stop!")
while x == 0:                                                         
  query = input("Ask your question: ").lower()                         # lower used to ensure "break" works
  if query == "break":
    print("ok bye!")
    break
  else:
    random_list = random.choice(answers)                               # randomises list chosen
    answer = random.choice(random_list)                                # randomises answer from the list
    print(answer)
