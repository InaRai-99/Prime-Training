# Count down with custom steps

start = 80
end = 0
step = -5
current = start

print("Countdown:")
while current > end:
    print(current)
    current += step
else:
    print("Ignition!")