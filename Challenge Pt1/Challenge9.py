text = "Hello Python"
encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")
if decoded == text:
    print("Encoding and decoding successful.")
    print("Encoded:", encoded)
else:
    print("Mismatch in decoding.")