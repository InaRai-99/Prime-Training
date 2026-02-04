# Count specific byte

b = b"Mango"
count = 0
for byte in b:
    if byte == 97:
        count += 1
else:
    print("Byte 'a' occurs", count, "times.")