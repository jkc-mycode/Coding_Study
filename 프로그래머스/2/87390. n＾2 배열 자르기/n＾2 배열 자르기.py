def solution(n, left, right):
    result = []
    for i in range(left//n, right//n+1):
        result += [i+1] * (i+1) + list(range(i+2, n+1))
    
    return result[left % n:left % n + (right-left) + 1]