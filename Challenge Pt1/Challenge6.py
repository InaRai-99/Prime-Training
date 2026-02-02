sentence = "apple banana apple orange"
words = sentence.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
else:
    print("Frequencies:", freq)
    print("Unique words:", set(words))