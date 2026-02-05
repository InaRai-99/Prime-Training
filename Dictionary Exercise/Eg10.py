# Find key with highest value

scores = {"Wayne": 99, "Kent": 98, "Diana": 97}
highest = list(scores.keys())[0]
for name in scores:
    if scores[name] > scores[highest]:
        highest = name
else:
    print("Top scorer:", highest, "with", scores[highest]) 