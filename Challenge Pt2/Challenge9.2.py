# Count word frequencies in text

text = "Pineapple Cherry Kiwi Lemon Cherry Kiwi Watermelon Cherry Lemon"
words = text.split() 
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word frequencies:")
for word, count in freq.items():
    print(f"{word}: {count}")