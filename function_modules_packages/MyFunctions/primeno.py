def is_prime(number):
    if(number<=1):
        return False
    for i in range(2,number):
        if(number%i ==0):
            return False
    return True

r = is_prime(39)
print(r)