#Check Password Strength

Password = "GuessThis26"
if len(Password)<6:
    print("Weak Password")
elif Password.isalnum() and any (ch.isdigit()for ch in Password):
    print("Strong Password")
else:
    print("Password needs numbers and letters.")