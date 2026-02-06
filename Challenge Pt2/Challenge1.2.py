# Generate multiplication table for a number

number = 9
counter = 1

while counter <= 15:
    result = number * counter
    print(f"{number} x {counter} = {result}")
    counter += 1
else:
    print("Multiplication table complete!")