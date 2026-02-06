# Calculate student grade average

grades = [79.5, 86.0, 95.5, 100.0, 40.5]
total = 0.0
count = 0

for grade in grades:
    total += grade
    count += 1

average = total / count
print(f"Average grade: {average:.2f}")

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
else:
    print("Grade: D")