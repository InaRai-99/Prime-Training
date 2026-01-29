def add_item(item,shopping_list=None):
    if shopping_list is None:
        shopping_list=[]
    
    shopping_list.append(item)
    return shopping_list
def checkout(total):
    if(total==0):
        print("Nothing to Checkout")
    elif total<0:
        print("ERR")
    else:
        print(f"Total is £ {total}")

items = add_item("Orange")
items = add_item("Strawberry",items)
items = add_item("Kiwi",items)
items = add_item("Watermelon",items)
items = add_item("Lemon",items)
total = 0
for i in items:
    total+=6
checkout(total)

def add_item(item,shopping_list=[]):
    shopping_list.append(item)
    return shopping_list
def checkout(total):
    if(total==0):
        print("Nothing To Checkout")
    elif total<0:
        print("ERR")
    else:
        print("Total is £", total)
        
items = add_item("Orange")
items = add_item("Strawberry")
total = 0
for i in items:
    total+=6
checkout(total)

def add_item(item,shopping_list=[]):
    shopping_list.append(item)
    return shopping_list
def checkout(total):
    if(total==0):
        print("Nothing To Checkout")
    elif total<0:
        print("ERR")
    else:
        print ("Total is £",total)
        
items = add_item("Orange")
items = add_item("Strawberry")
total = 0
for i in items:
    total+=6
checkout(total)

#def is_even(num):
    #if num % 2 == 1:
        #return True
    #else:
        #return False
    
#print(is_even(4))