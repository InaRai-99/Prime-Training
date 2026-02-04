# Generate a sequence of complex numbers

count = 1
z = 80 + 97j
while count <= 7:
    print("Complex number:", z)
    z = z + 1 + 3j
    count += 1
else:
    print("Sequence complete.")