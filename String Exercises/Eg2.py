#Count vowels in a string

Text = "Welcome to the Earth!"
Vowels = "AEIOU aeiou"
Count = 0
for char in Text:
    if char in Vowels:
        Count +=1
else:
    print("Numbers of Vowels:",Count)