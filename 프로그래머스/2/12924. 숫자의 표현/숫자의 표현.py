def solution(n):
    result = 0
    
    for i in range(1, n+1):
        num = 0
        for j in range(i, n+1):
            num += j
            if num >= n:
                break
        if num == n:
            result += 1
    
    return result