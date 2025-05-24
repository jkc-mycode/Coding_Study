from collections import Counter

def solution(want, number, discount):
    result = 0
    want_dict = {want[i]: number[i] for i in range(len(want))}
    
    for i in range(len(discount)-9):
        discount_dict = dict(Counter(discount[i:i+10]))
        flag = True
        
        for w in want:
            if discount_dict.get(w) == None or discount_dict[w] < want_dict[w]:
                flag = False
                break
                
        if flag: result += 1
    
    return result
    