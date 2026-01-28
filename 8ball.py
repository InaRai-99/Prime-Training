import random
possible_answers=["Yes",
                  "No",
                  "Maybe",
                  "Sure",
                  "Absolutely",
                  "Try Again",
                  "Doubtful",
                  " No Way"]
que = input ("Ask the Magic 8-ball a question")
ans = random.choice(possible_answers)
print ("Magic 8_balls says:", ans)