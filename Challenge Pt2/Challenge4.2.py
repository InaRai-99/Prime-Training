# Decode message by shifting characters

encoded = "Kwqql ? havzx"
decoded = ""
shift = 1

for char in encoded:
    if char.isalpha():
        new_char = chr(ord(char) - shift)
        decoded += new_char
    else:
        decoded += char

print(f"Original: {encoded}")
print(f"Decoded: {decoded}")