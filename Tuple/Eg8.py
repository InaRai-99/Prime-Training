# Find the largest number

nums = (90, 567, 890, 456)
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
else:
    print("Largest number:", largest)