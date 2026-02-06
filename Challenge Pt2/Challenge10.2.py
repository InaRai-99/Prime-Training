# Filter duplicate sensor readings

readings = [33.8, 31.9, 24.8, 31.9, 20.4, 33.8]
unique = set()
duplicates = set()

for value in readings:
    if value in unique:
        duplicates.add(value)
    else:
        unique.add(value)

print(f"Original: {len(readings)} readings")
print(f"Unique values: {unique}")
print(f"Duplicate values: {duplicates}")