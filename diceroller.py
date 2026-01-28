import random
possible_answers=["1",
                  "2",
                  "3",
                  "4",
                  "5",
                  "6"]
que = input ("Roll the dice once")
ans = random.choice(possible_answers)
print ("Dice Number is", ans)