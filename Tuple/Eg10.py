# Unpack tuple values

person = ("Bruce", 36, "Gotham")
if len(person) == 3:
    name, age, city = person
    print("Name:", name, "Age:", age, "City:", city)
else:
    print("Tuple does not have exactly 3 elements.")