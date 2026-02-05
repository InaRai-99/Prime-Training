# Union of two sets

set1 = {"Pineapple", "Strawberry"}
set2 = {"Lemon", "Grapes", "Strawberry"}
union_set = set1 | set2
if len(union_set) == 4:
    print(union_set)
else:
    print("Union size mismatch.")