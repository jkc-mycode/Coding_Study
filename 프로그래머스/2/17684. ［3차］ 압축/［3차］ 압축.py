def solution(msg):
    result = []
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic = {alpha[i]: i+1 for i in range(len(alpha))}
    count = len(dic) + 1
    
    i = 0
    while i < len(msg):
        j = i + 1
        while j <= len(msg) and dic.get(msg[i:j]) != None:
            j += 1
        
            w = msg[i:j-1]
        result.append(dic[w])

        if j <= len(msg):
            dic[msg[i:j]] = count
            count += 1

        i += len(w)
    
    return result