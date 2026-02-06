# Track and update product inventory

inventory = {"A110": 20, "B809": 90, "C777": 50}
sales = [("A110", 13), ("B809", 17), ("A110", 2)]

for item, qty in sales:
    if qty <= inventory.get(item, 0):
        inventory[item] -= qty
        print(f"Sold {qty} of {item}")
    else:
        print(f"Not enough {item} in stock")

print("\nRemaining inventory:")
for item, stock in inventory.items():
    print(f"{item}: {stock}")