from random import randrange, seed
seed(5)
for i in range (0, 1):
    x = randrange(1, 101)
    
done = False
tries = 0
while not done:
    value = int(input("Guess a value from 1 to 100: "))
    if value > x:
        print("Too high, please try again")
        tries += 1
    elif value < x:
        print("Too low, please try again")
        tries += 1
    elif value == x:
        print(value, "is the correct answer")
        tries += 1
        print("It took you ", tries, " to get the correct answer")
        done = True
    