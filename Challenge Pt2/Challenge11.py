# Process student records with mixed types

students = [
    {"id": 111, "name": "Aaron", "grades": (56, 82, 98)},
    {"id": 112, "name": "Eric", "grades": (86, 98, 100)}
]

for student in students:
    print(f"\nProcessing {student['name']} (ID: {student['id']})")
    total = 0
    for grade in student['grades']:
        total += grade
    
    avg = total / len(student['grades'])
    print(f"Average grade: {avg:.1f}")
    
    if avg >= 90:
        status = "A"
    elif avg >= 80:
        status = "B"
    else:
        status = "C"
    print(f"Status: {status}")