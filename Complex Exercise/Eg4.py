# Divide complex numbers

a = 57 + 93j
b = 42 + 10j
result = a / b
if result.imag > 0:
    print("Division result:", result)
else:
    print("Imaginary part non-positive.")