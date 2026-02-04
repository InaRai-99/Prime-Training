# Convert bytes back to string

b = b"Goodbye"
decoded = b.decode("utf-8")
if decoded == "Goodbye":
    print("Decoded string:", decoded)
else:
    print("Decoding failed.")