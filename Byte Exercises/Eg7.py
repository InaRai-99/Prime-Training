# Create bytes from integers

byte_array = bytes([78, 79, 80])
if byte_array == b"DEF":
    print(byte_array)
else:
    print("Bytes creation failed.")