# Remove spaces from bytes

data = b"Welcome Home"
result = b""
i = 0
while i < len(data):
    if data[i] != 32:  
        result += bytes([data[i]])
    i += 1
else:
    print(result)