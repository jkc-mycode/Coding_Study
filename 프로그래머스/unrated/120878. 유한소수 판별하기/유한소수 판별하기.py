def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def solution(a, b):
    n = gcd(a, b)
    a, b = a // n, b // n
    
    d = 2
    while d <= b:
        if b % d == 0:
            if d not in [2, 5]: return 2
            b /= d
        else:
            d += 1
    
    return 1
    
    
    