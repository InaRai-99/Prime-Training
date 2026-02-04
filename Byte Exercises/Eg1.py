# Convert string to bytes

Text = "Goodbye"
byte_data = Text.encode("utf-8")
if isinstance(byte_data, bytes):
    print(byte_data)
else:
    print("Conversion failed.")