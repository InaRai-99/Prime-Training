balance = 1000
def display_balance(bal):
    print (f"Balance is £{bal}")
def deposit(bal,amount):
    if (amount<=0):
        print("Deposit amount must be Positive")
        return bal
    print("Deposit Done, Current Balance", bal+amount)
    return bal+amount
def withdraw(bal,amount):
    if (amount<=0):
        print("Withdraw Must be Positive.")
        return bal
    if (amount >bal):
        print("Insufficient Funds")
        return bal
    print ("Withdrawal done, Current Balance", bal-amount)
    return bal-amount
while True:
    print("\nATM")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input ("Choose an Option 1-4")
    if (choice =="1"):
        display_balance(balance)
    elif (choice =="2"):
        try:
            amount =  float(input("Enter Deposit Amount"))
            balance = deposit(balance,amount)
        except ValueError:
            print("INVALID Input Please Enter Numeric Value")
    elif (choice =="3"):
        try:
            amount = float(input("Enter Withdrawal Amount"))
            balance = withdraw(balance,amount)
        except ValueError:
            print("INVALID Input Please Enter Numeric Value")
    elif (choice =="4"):
        print("THANK YOU FOR USING ATM, BYE")
        break
    else:
        print("INVALID Choice, Press Any Number Between 1-4")