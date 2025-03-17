from collections import Counter

def solution(want, number, discount):
    result = 0
    want_dict = {want[i]: number[i] for i in range(len(want))}
    for i in range(len(discount)-9):
        discount_count = Counter(discount[i:i+10])
        temp = 0
        for j in want:
            if discount_count.get(j) and want_dict[j] <= discount_count[j]:
                temp += 1
            else:
                break
        if temp == len(want):
            result += 1
    
    return result