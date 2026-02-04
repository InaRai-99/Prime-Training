#Remove spaces from a string

Text = "Welcome to London"
Result = ""
i = 0
while i < len(Text):
    if Text[i] != "":
        Result +=Text[i]
    i += 1
else:
    print("String without spaces:", Result)