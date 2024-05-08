def solution(t, p):
    result = 0
    for i in range(0, len(t)):
        if len(t[i:len(p)+i:]) == len(p) and int(t[i:len(p)+i:]) <= int(p):
            result += 1
            
    return result
    