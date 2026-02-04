#Convert USD to EUR

Rate = 0.98
for USD in range(10,21):
    EUR = USD * Rate
    print(USD, "USD =", round (EUR,2), "EUR")
else:
    print ("Conversion Complete.")