def solution(n):
    result = 1000000
    for i in range(1, n):
        if n % i == 1 and result > i:
            result = i
            break;
    return result