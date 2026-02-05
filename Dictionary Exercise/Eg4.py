# Remove all keys from dictionary

d = {"g": 7, "h": 8}
while d:
    key = list(d.keys())[0]
    del d[key]
else:
    print("All keys removed.", d)