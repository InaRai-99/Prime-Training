accounts = {"A123": 1500.0, "B456": 2500.0}
valid_accounts = set(accounts.keys())
total_balance = 0
for acc in valid_accounts:
    total_balance += accounts[acc]
else:
    print("Balances:", accounts)
    print("Total balance:", total_balance)