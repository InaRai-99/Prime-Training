# Attempt to modify a tuple

colours = ("Pink", "Orange", "Black")
try_index = 1
if try_index < len(colours):
    print("Tuples are immutable. Cannot change:", colours[try_index])
else:
    print("Index out of range.")