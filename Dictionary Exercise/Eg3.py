# Update value in dictionary

item = {"item": "Lamp", "Price": 290}
if "Price" in item:
    item["Price"] = 15
    print("Updated dictionary:", item)
else:
    print("Price key missing.")