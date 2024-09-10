import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if (num % i == 0):
            return False
    return True

def solution(n):
    result = 1
    for i in range(3, n+1):
        if (isPrime(i)):
            result += 1
    return result