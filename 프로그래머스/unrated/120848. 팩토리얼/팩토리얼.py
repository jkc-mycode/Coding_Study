def factorial(k):
    if k == 0:
        return 1
    return k * factorial(k-1)

def solution(n):
    for i in range(1, n+2):
        if factorial(i) > n:
            return i-1
        
        
        
        