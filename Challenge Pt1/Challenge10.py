names = {"Alice", "Bob"}
marks = [85, 90, 78, 92]
avg = sum(marks) / len(marks)
report = {"avg_score": avg, "total_students": len(names)}
progress = range(1, len(marks) + 1)
for p in progress:
    print("Progress step:", p)
else:
    print("Report:", report)