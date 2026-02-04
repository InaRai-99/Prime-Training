#Print numbers, skipping those divisible by 7

for i in range (20,50):
    if i%7 == 0:
        continue 
    print (i)
else:
    print("Skipped numbers divisible by 7.")