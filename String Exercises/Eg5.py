#Count occurence of "apple"

Sentence = "Strawberry Watermelon Jackfruit Mango Cherry"
Words = Sentence.split()
Count = 0
for W in Words:
    if W == "Strawberry":
        Count +=1
else:
    print("Word 'Strawberry' occurs",Count, "times." )