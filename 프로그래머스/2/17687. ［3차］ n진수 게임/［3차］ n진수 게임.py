def to_base(n, base):
    result = ""
    digits = "0123456789ABCDEFG"
    if n == 0:
        return "0"
    while n:
        result = digits[n % base] + result
        n //= base
    return result
    

def solution(n, t, m, p):
    result = ""
    
    for i in range(t*m):
        result += to_base(i, n)

    result = "".join(result[i] for i in range(p-1, len(result), m))
    return result[:t]