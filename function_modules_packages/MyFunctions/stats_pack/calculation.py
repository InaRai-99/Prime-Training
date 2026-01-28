def rect_area(l,b):
    return l*b

def highest (a,b):
    if (a>b):
        return a
    return b
def is_prime(number):
    if (number<1):
        return False
    for i in range (2, number):
        if(number%1 ==0):
            return False
        return True