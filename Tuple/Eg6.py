# Count how many times 'apple' occurs

fruits = ("Pineapple", "Strawberry", "Pear")
count = 0
for fruit in fruits:
    if fruit == "Pineapple":
        count += 1
else:
    print("Pineapple occurs", count, "times.")