#Count occurrences of 4

Nums = [4,6,9,8,4,2,4]
Count = 0
for n in Nums:
    if n == 4:
        Count += 1
else:
    print ("4 appears", Count, "times.")