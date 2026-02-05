# Count word frequency in a sentence

sentence = "Rose Peony Lily Lotus"
freq = {}
for word in sentence.split():
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
else:
    print(freq)