def solution(n):
    result = 0
    num = n + 1
    
    while True:
        bin_n = bin(n)[2:]
        bin_num = bin(num)[2:]
        if bin_n.count('1') == bin_num.count('1'):
            result = num
            break
        num += 1
    
    return result