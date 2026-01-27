students =[
    {"name":'s1', "score":95},
    {"name":'s2', "score":82},
    {"name":'s3', "score":98},
    {"name":'s4', "score":65},
]
h_score =0
topper=""
for student in students:
    if (student["score"]>h_score):
        h_score = student["score"]
        topper=student["name"]
print ("Student with Highest Score is", topper)