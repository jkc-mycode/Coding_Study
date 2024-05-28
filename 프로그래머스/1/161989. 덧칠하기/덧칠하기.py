import math

def solution(n, m, section):
    # result = section[-1] - section[0] + 1
    # return math.ceil(result / m)
    arr = list(1 for i in range(n))
    for i in section:
        arr[i-1] = 0
    
    result = 0
    for i in range(n):
        if arr[i] == 0:
            result += 1
            for j in range(m):
                if i + j > n - 1:
                    break;
                arr[i+j] = 1
    return result
    
        
    