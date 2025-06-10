def to_base_k(num, base):
    digits = '0123456789'
    result = ''
    
    if num == 0: return '0'
    
    while num > 0:
        result = digits[num % base] + result
        num //= base
    return result

def is_prime(num):
    if num < 2: return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True

def solution(n, k):
    result = 0
    k_base = to_base_k(n, k)
    
    for num in k_base.split('0'):
        if num != '' and is_prime(int(num)):
            result += 1
    
    return result
    