# Multiply complex numbers

num1 = 38 + 46j
num2 = 72 + 58j
product = num1 * num2
if product.real < 0:
    print("Product:", product)
else:
    print("Real part is non-negative.")