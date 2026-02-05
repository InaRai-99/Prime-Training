# Add elements to a set

numbers = set()
to_add = [4, 5, 6]
i = 0
while i < len(to_add):
    numbers.add(to_add[i])
    i += 1
else:
    print("Final set:", numbers)