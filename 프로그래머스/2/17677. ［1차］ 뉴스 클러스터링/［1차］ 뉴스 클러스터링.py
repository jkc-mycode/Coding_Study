def solution(str1, str2):
    def set_str(s):
        s = s.lower()
        return [s[i:i+2] for i in range(len(s)-1) if s[i].isalpha() and s[i+1].isalpha()]
    
    g1 = set_str(str1)
    g2 = set_str(str2)
    intersection = []
    union = g1[:]
    
    for element in g1:
        if element in g2:
            intersection.append(element)
            g2.remove(element)
    
    union.extend(g2)
    
    if len(union) == 0 and len(intersection) == 0:
        return 65536
    
    return int(len(intersection) / len(union) * 65536)
