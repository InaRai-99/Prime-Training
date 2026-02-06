# Find prime numbers in a range

n = 55
primes = []
candidate = 2

while candidate <= n:
    is_prime = True
    for divisor in primes:
        if divisor * divisor > candidate:
            break
        if candidate % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(candidate)
    candidate += 1

print(f"Primes up to {n}:")
print(primes)