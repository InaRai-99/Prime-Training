# Remove duplicates from a list using set

nums = [9, 7, 8, 6, 7, 7]
unique_nums = list(set(nums))
if len(unique_nums) == 4:
    print(unique_nums)
else:
    print("Unexpected number of unique elements.")