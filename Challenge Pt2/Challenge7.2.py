# Calculate distance between points

pointA = (8, 5)
pointB = (25, 35)
squares = 0

for coord in zip(pointA, pointB):
    diff = coord[1] - coord[0]
    squares += diff ** 2

distance = squares ** 0.5
print(f"Distance between {pointA} and {pointB}: {distance:.2f} units")