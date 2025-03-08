def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    result = 1
    for i in arr:
        result = lcm(result, i)
    
    return result
        