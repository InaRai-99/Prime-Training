# Compare real and imaginary parts

values = [9+8j, 5+7j, 3+6j]
for v in values:
    if v.imag > v.real:
        print(v, "- Imaginary part is greater.")
    elif v.imag == v.real:
        print(v, "- Real and imaginary are equal.")
    else:
        print(v, "- Real part is greater.")
else:
    print("Comparison complete.")