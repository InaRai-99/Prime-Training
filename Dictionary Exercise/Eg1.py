# Create a dictionary and add key-value pairs

data = {}
keys = ['d', 'e', 'f']
values = [4, 5, 6]
i = 0
while i < len(keys):
    data[keys[i]] = values[i]
    i += 1
else:
    print("Dictionary filled:", data)