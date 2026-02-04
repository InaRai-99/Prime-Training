# Find the longest word in a sentence

Text = "Alligator Hippo Bear Bee Platypus"
Longest = ""
for w in Text.split():
    if len(w) > len(Longest):
        Longest = w
else:
    print ("Longest Word:", Longest)