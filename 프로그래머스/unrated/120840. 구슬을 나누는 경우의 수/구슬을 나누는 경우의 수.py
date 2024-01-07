def factorials(n):
    value = 1
    for i in range(2, n+1):
        value *= i
    
    return value

def solution(balls, share):
    return int(factorials(balls) / (factorials(balls-share) * factorials(share)))