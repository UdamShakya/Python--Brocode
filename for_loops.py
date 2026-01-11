for x in range(1,21,2):
    print(x)    

for x in range(1,21):
    if x== 13:
        break
    else: 
        print(x)

#countdown timer 

import time

#time.sleep(3)

my_time= int(input("Enter time in seconds: "))

for x in range (my_time,0,-1):
    seconds= x % 60
    minutes= int(x / 60)%60
    hours = int(x / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")



# nested loops 

for y in range(3):
    for x in range (1,10):
        print(x, end="")
    print()

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol to use: ")

for y in range(rows):
    for x in range(columns):
        print(symbol, end="")
    print()

