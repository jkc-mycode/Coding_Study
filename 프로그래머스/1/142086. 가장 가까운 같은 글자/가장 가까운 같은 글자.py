def solution(s):
    result = [];
    temp = [];
    
    for i in range(len(s)):
        if s[i] not in temp:
            temp.append(s[i])
            result.append(-1)
        else:
            minVal = 9999
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    if minVal > (i - j):
                        minVal = i - j
                    result.append(minVal)
                    temp.append(s[i])
                    break
    return result
                    