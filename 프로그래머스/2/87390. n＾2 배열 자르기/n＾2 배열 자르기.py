def solution(n, left, right):
    result = []
    for i in range(left, right+1):
        result.append(max(i//n, i%n)+1)
    
    return result
        