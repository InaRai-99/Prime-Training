import random
s = random.randint(1,100)
guess = None
while s!=guess:
    guess= int(input("guess no b/w 1 ---100"))
    if (guess<s):
        print("too low")
    elif (guess>s):
        print("too high")
    else:
        print("YOU WON")