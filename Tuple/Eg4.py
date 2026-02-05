# Access elements in nested tuple

nested = (6, 7, (8, 9))
if isinstance(nested[2], tuple):
    print("Nested element:", nested[2][0])
else:
    print("No nested tuple found.")