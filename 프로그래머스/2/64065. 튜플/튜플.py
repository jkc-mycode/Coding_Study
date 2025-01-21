import json

def solution(s):
    formated_str = s.replace('{','[').replace('}',']')
    formated_list = list(map(list, json.loads(formated_str)))
    formated_list.sort(key=len)
    result = [formated_list[0][0]]
    
    for i in range(len(formated_list)-1):
        diff = [j for j in formated_list[i+1] if j not in formated_list[i]]
        result += diff
        
    return result