def solution(n):
    result = 1
    
    for i in range(1, n):
        temp = 0
        for j in range(i, n):
            temp += j
            if temp >= n:
                break
        if temp == n:
            result += 1
    
    return result