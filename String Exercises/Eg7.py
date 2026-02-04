#Check if a string contains digits

Data = "France987"
for ch in Data:
    if ch.isdigit():
        print("Contains Digits.")
        break
else:
    print ("No Digits Found.") 