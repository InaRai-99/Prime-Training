#Reverse a list manually

original = [9,8,7,6]
reversed_list = []
i = len(original) -1
while i>= 0:
    reversed_list.append(original[i])
    i -=1
else:
    print("Reversed list:", reversed_list)