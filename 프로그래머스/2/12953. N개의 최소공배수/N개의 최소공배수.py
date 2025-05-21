def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcd(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    if len(arr) == 1: return arr[0]
    if len(arr) == 2: return lcd(arr[0], arr[1])
    result = lcd(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        result = lcd(arr[i], result)
    
    return result