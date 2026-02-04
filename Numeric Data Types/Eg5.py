#Guess the secret number

secret = 20
guess = 0
while guess!= secret:
    guess += 1 #trying numbers 1, 2, 3..
    print ("Guessing", guess)
else:
    print("Correct! The secret number is ", secret )