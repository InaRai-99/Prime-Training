# Merge two dictionaries manually

d1 = {"i": 9, "j": 10}
d2 = {"k": 11}
for key in d2:
    d1[key] = d2[key]
else:
    print("Merged dictionary:", d1)