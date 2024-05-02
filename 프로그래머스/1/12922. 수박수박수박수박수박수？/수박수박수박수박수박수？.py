def solution(n):
    result = ''
    
    for i in range(1, n + 1):
        if i % 2 == 0: result += '박'
        else: result += '수'
    return result