# Check if temperatures are below freezing

temperatures = [8, -3, 7, -3, 0, 13, -6, -10]
negative_count = 0

for temp in temperatures:
    if temp < 0:
        print(f"{temp}°C: Freezing!")
        negative_count += 1
    elif temp == 0:
        print("0°C: Ice point!")
    else:
        print(f"{temp}°C: Above freezing")

print(f"Total freezing days: {negative_count}")