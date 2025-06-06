def to_base_n(num, base):
    digits = "0123456789ABCDEFG"
    result = ""
    
    if num == 0: return '0'
    
    while num > 0:
        result = digits[num % base] + result
        num //= base
    
    return result

def solution(n, t, m, p):
    result = ''
    
    for i in range(t*m):
        result += to_base_n(i, n)

    return "".join(list(result)[p-1:t*m:m])
    