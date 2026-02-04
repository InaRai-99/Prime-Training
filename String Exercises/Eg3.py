#Reverse a string using while loop

Original = "Anaconda"
Reversed_Text = ""
i = len(Original)-1
while i >=0:
    Reversed_Text += Original[i]
    i -= 1
else:
    print("Reversed String:", Reversed_Text)