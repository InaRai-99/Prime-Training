# Identify quadrant of complex numbers

numbers = [9+5j, -7+9j, -8-4j, 6-1j]

for num in numbers:
    real = num.real
    imag = num.imag
    print(f"Number: {num}")
    
    if real > 0 and imag > 0:
        print("Quadrant I")
    elif real < 0 and imag > 0:
        print("Quadrant II")
    elif real < 0 and imag < 0:
        print("Quadrant III")
    else:
        print("Quadrant IV")