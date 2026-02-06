# Generate grid coordinates

rows = range(2, 5)
cols = range(3, 6)
grid = []

for r in rows:
    for c in cols:
        grid.append((r, c))

print("3x4 Grid Coordinates:")
print(grid)