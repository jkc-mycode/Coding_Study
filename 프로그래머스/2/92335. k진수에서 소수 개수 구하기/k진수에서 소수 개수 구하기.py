def to_base_k(num, base):
    digit = '0123456789'
    temp = ''
    while num > 0:
        temp = digit[num % base] + temp
        num //= base
    
    return temp

def is_prime(num):
    if num < 2: return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True
    
def solution(n, k):
    result = 0
    k_base = to_base_k(n, k).split('0')
    
    for num in k_base:
        if num and is_prime(int(num)):
            result += 1
    
    return result
    
    