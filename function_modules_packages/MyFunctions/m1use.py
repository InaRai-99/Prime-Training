from m1 import count_vowels, reverse_string
str  = input("Enter any String")
option = input("Press 1 for Vowel Count, Press 2 for Reverse String")
if (option =="1"):
    x = count_vowels(str)
    print("No of Vowels in the Entered String is", x)
else:
    r = reverse_string(str)
    print("Reversed String is:", r)