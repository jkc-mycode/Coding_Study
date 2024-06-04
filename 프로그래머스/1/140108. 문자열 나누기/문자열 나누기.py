def solution(s):
    result = []
    same, diff = 0, 0
    temp = s
    
    for i in range(len(temp)):
        if (s[0] == temp[i]):
            same += 1
        else:
            diff += 1
        
        if(same == diff):
            result.append(s[0:same+diff])
            s = temp[i+1:]
            same, diff = 0, 0
    if s != '':
        result.append(s)
        
    return len(result)
    