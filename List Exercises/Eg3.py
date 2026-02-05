#Removing all items from the list

Numbers = [9,8,7]
while Numbers:
    removed =  Numbers.pop()
    print ("Removed:", removed)
else:
    print ("All items removed. List is empty:", Numbers)