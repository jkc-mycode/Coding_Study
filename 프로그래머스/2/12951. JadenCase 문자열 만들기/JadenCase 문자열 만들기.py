def solution(s):
    result = ''
    s = s.lower()
    if s[0].isalpha():
        result += s[0].upper()
    else:
        result += s[0]
    
    for i in range(1, len(s)):
        if s[i].isalpha() and s[i-1] == ' ':
            result += s[i].upper()
        else:
            result += s[i]
    
    return result