def solution(n):
    origin_bin_num = bin(n)[2:]
    
    while True:
        n += 1
        bin_num = bin(n)[2:]
        if origin_bin_num.count('1') == bin_num.count('1'):
            break
    
    return n
        
