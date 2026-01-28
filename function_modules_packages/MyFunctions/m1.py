def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count = count+1
            count +=1
    return count
def reverse_string(str):
    rs=""
    for char in str:
        rs=rs+char  
    return rs