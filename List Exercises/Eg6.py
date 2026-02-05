#Sort a list manually

nums = [9,8,7,6]
sorted_list = []
while nums:
    smallest = nums[0]
    for n in nums:
        smallest = n
nums.remove(smallest)
sorted_list.append(smallest)
else:
    print("Sorted list:", sorted_list)