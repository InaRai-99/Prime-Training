inventory = {}
items = ["apple", "banana", "apple", "orange"]
unique_items = set(items)
for item in unique_items:
    inventory[item] = inventory.get(item, 0) + 1
else:
    print("Final inventory:", inventory)