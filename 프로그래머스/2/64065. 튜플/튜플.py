def solution(s):
    s = sorted([i.split(',') for i in s[2:-2].split('},{')], key=lambda x: len(x))
    result = [int(s[0][0])]
    
    for i in range(1, len(s)):
        temp = [value for value in s[i] if value not in s[i-1]]
        result.append(int(temp[0]))
    
    return result
            