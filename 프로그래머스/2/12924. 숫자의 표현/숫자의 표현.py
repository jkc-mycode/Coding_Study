def solution(n):
    result = 0
    
    for i in range(1, n+1):
        cur_sum = 0
        for j in range(i, n+1):
            cur_sum += j
            if cur_sum == n:
                result += 1
                break
            
            if cur_sum > n:
                break
        
    return result