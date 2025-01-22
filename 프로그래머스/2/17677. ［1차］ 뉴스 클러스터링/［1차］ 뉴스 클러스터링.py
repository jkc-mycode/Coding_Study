def set_str(s):
    s = s.lower()
    s = [s[i]+s[i+1] for i in range(len(s)-1)]
    result = []
    for i in s:
        if i[0].isalpha() and i[1].isalpha():
            result.append(i)
            
    return result

def solution(str1, str2):
    str1 = set_str(str1)
    str2 = set_str(str2)
    intersection = []
    union = str1[:]
    
    for i in str1:
        if i in str2:
            intersection.append(i)
            str2.remove(i)
    union.extend(str2)
    
    if len(intersection) == 0 and len(union) == 0:
        return 65536
    
    return int(len(intersection) / len(union) * 65536)
    
