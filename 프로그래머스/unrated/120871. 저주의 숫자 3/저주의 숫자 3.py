def solution(n):
    val = []
    d = 1
    while len(val) <= n:
        if d % 3 != 0 and '3' not in str(d):
            val.append(d)
        d += 1
    
    return val[n-1]
        