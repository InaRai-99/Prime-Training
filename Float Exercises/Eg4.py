#Deduct amount until balance is too low.

Balance = 470.50
Withdrawal = 235.60
while Balance > 50.0:
    print("Balance before withdrawal:", Balance)
    Balance -= Withdrawal
else:
    print("Low Balance Warning. Final Balance:", Balance)