items = ("milk", "bread", "eggs")
prices = {"milk": 1.5, "bread": 2.0, "eggs": 3.0}
total = 0.0
for i in range(len(items)):
    total += prices[items[i]]
else:
    print("Purchased items:", items)
    print("Total price:", total)