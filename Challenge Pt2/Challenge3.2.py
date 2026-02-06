# Find complex numbers with magnitude > 5

values = [9+3j, 8+5j, 3+3j, 1+2j, 8+7j]
threshold = 5
count = 0

for val in values:
    magnitude = (val.real**2 + val.imag**2)**0.5
    if magnitude > threshold:
        count += 1
        print(f"{val} has magnitude {magnitude:.2f} (>5)")

print(f"{count} numbers exceed magnitude 5")
