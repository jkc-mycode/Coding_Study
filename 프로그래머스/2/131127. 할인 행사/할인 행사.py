from collections import Counter

def solution(want, number, discount):
    result = 0
    want_dict = {want[i]: number[i] for i in range(len(want))}
    
    for i in range(len(discount)-9):
        discount_dict = dict(Counter(discount[i:i+10]))
        
        if discount_dict == want_dict:
            result += 1
    
    return result
    
