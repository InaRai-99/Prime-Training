#Find the largest number in a list

numbers =  [190,834,567,3921,7654,80,1]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
else: 
    print("The largest number is: ", largest)