# nested loops - loop inside another loop :3
symbol = ""


rows = int(input("how many rows: "))
columns = int(input("how many columns: "))
symbol = input("what symbol to use: ")

# loop time -- symbol  

while len(symbol) != 1: 
    print ("only one symbol pls!!")
    symbol = input("what symbol to use: ")

# loop end -- symbol

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")  # prints symbol without a line break
    print()                    # will print a new line