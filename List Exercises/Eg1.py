#Adding items to a shopping list

Shopping_list = []
Items = ["Fruits", "Juice", "Wine", "Shampoo", "Charger"]
i = 0
while i <len(Items):
    Shopping_list.append([Items[i]])
    print("Added:",Items[i])
    i +=1
else:
    print("Shopping list complete:", Shopping_list)
