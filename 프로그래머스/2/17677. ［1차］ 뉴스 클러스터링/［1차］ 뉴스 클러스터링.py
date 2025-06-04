from collections import Counter
import math

def solution(str1, str2):
    str1_list = []
    str2_list = []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append((str1[i]+str1[i+1]).lower())
    
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_list.append((str2[i]+str2[i+1]).lower())
    
    if not str1_list and not str2_list:
        return 65536
    
    shared_list = list((Counter(str1_list) & Counter(str2_list)).elements())
    merged_list = list((Counter(str1_list) | Counter(str2_list)).elements())
    
    if not shared_list:
        return 0
    else:
        return math.floor(len(shared_list)/len(merged_list) * 65536)