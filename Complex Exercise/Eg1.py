# Add two complex numbers

a = 64 + 10j
b = 78 + 58j
sum_complex = a + b
if sum_complex.imag > 0:
    print("Sum:", sum_complex)
else:
    print("No imaginary part.")