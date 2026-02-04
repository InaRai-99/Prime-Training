#ATM withdrawal simulation

balance = 60
withdraw = 15
while balance >- withdraw:
    print("Withdrawing", withdraw)
    balance -=withdraw
else:
    print("No more funds. Remaining balance:", balance)