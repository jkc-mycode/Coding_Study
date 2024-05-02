def solution(a, b):
    result = 0
    return sum(a[i] * b[i] for i in range(len(a)))