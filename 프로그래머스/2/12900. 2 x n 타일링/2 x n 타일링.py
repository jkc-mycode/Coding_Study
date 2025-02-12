def solution(n):
    result = [0 for _ in range(n+1)]
    if n == 0:
        return 0
    
    result[1] = 1
    result[2] = 2
    for i in range(3, n+1):
        result[i] = (result[i-1] + result[i-2]) % 1000000007
    
    return result[-1]