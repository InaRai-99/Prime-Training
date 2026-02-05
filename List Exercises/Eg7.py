#Check for duplicates

numbers = [9,8,1,4,2,1,6,1]
seen = []
for n numbers:
    if n in seen:
        print("Duplicate found:", n)
        break
    else:
        seen.append(n)
else:
    print("No duplicates found.")