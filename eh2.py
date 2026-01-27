try:
    f = open ("demo.txt", "r")
    data = f.read()
    n = int(" no")
    print(data)
finally:
    f.close()
    print("file closed")