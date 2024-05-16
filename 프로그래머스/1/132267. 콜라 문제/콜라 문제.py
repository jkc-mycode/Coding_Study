def solution(a, b, n):
    result = 0
    
    while n >= a:
        result += int(n / a) * b
        n = int(n / a) * b + n % a
    return result