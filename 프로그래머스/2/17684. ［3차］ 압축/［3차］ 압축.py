def solution(msg):
    result = []
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dic = {alpha[i]: i+1 for i in range(len(alpha))}
    count = len(dic) + 1
    
    while True:
        if dic.get(msg) != None:
            result.append(dic[msg])
            break
        for i in range(1, len(msg)+1):
            if dic.get(msg[0:i]) == None:
                result.append(dic[msg[0:i-1]])
                dic[msg[0:i]] = count
                count += 1
                msg = msg[i-1:]
                break
                
    return result