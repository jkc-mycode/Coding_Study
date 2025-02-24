from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    
    for size in course:
        combs = []
        for order in orders:
            combs.extend(combinations(sorted(order), size))
        
        count = Counter(combs)
        if count:
            max_count = max(count.values())
            if max_count > 1:
                for key, value in count.items():
                    if value == max_count:
                        result.append("".join(key))
    
    return sorted(result)


# 70% 정답 코드
# def solution(orders, course):
#     result = []
#     combs = []
#     for size in course:
#         for order in orders:
#             combs.extend(combinations(sorted(order), size))
    
#     count = Counter(combs)
#     menus = {i: [] for i in course}
#     for key, value in count.items():
#         if value > 1 and len(key) in course:
#             menus[len(key)].append(["".join(key), value])
    
#     for key, value in menus.items():
#         if len(value) > 1:
#             menus[key] = sorted(value, key=lambda x: x[1], reverse=True)
#             i = 0
#             while len(menus[key]) > i and menus[key][0][1] == menus[key][i][1]:
#                 result.append(menus[key][i][0])
#                 i += 1
    
#     return sorted(result)