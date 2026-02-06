# Calculate circle properties

radius = 4.5
PI = 3.14159
step = 0.5

while radius <= 7.0:
    circumference = 2 * PI * radius
    area = PI * radius ** 2
    print(f"Radius: {radius:.1f}cm")
    print(f"Circumference: {circumference:.2f}cm")
    print(f"Area: {area:.2f}cm²\n")
    radius += step