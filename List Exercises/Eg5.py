#Find the largest number

numbers = [987, 765, 432]
max_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n
else:
    print("The Largest number:", max_num)