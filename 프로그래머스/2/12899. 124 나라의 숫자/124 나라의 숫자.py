from collections import deque

def solution(n):
    result = deque()
    
    while n > 0:
        if n % 3 == 0:
            n = n // 3 - 1
            result.appendleft('4')
        elif n % 3 == 1:
            n //= 3
            result.appendleft('1')
        elif n % 3 == 2:
            n //= 3
            result.appendleft('2')
    
    return "".join(result)