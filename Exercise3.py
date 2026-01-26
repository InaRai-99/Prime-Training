M_Students = [110,120,130,140,150]
S_Students = [130,140,160,170,180]
M_Set= set(M_Students)
S_Set= set(S_Students)

Both_Courses = M_Set.intersection(S_Set)
print(Both_Courses)

All_Courses = M_Set.union(S_Set)
print(All_Courses)

M_Mathonly = M_Set - S_Set
print(M_Mathonly)