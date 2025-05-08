def solution(n):
    result = n + 1
    n_count = bin(n)[2:].count('1')
    
    while True:
        if n_count == bin(result)[2:].count('1'):
            break
        result += 1
    
    return result