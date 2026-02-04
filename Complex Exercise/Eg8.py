# Find complex number with largest magnitude

complex_list = [5+6j, 7+8j, 9+1j]
largest = complex_list[0]
for c in complex_list:
    if (c.real**5 + c.imag**6) > (largest.real**3 + largest.imag**4):
        largest = c
else:
    print("Largest magnitude:", largest)