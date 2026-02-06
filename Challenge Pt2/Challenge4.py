# Validate username requirements

username = "VisualStudio_Account_999"
has_upper = False
has_digit = False

for char in username:
    if char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True

if len(username) >= 8:
    if has_upper and has_digit:
        print("Valid username!")
    else:
        print("Invalid: Needs uppercase letter and number")
else:
    print("Invalid: Too short (min 8 characters)")