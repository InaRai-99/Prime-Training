import math
marks = [35, 55, 60, 20, 15, 70]
sum_marks= math.fsum(marks)
print("Sum is", sum_marks)
length = len(marks)
print("Length is", length)
avg_marks = sum_marks/length
print("average is", math.floor(avg_marks))