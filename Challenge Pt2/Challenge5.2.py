# Create byte-based ASCII art

byte_values = [55, 42, 98, 12, 32]
art = b''
row = 1

while row <= 5:
    for byte_val in byte_values:
        char = bytes([byte_val])
        art += char * row + b' '
    art += b'\n'
    row += 1

print("ASCII Art:")
print(art.decode('utf-8'))