#Count how many times 8 appears

numbers = [8,9,3,7,8,10,8]
count = 0
for num in numbers:
    if num == 8:
        count+=1
else:
    print("8 appears", count, "times.")