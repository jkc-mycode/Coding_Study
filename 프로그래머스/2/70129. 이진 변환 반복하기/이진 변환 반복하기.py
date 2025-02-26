def solution(s):
    trans_count = 0
    remove_count = 0
    
    while s != '1':
        temp_s = s.replace('0', '')
        remove_count += (len(s) - len(temp_s))
        s = bin(len(s.replace('0', '')))[2:]
        trans_count += 1
    
    return [trans_count, remove_count]