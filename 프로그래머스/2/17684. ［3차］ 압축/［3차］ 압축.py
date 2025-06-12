def solution(msg):
    result = []
    words = {chr(65+i): i+1 for i in range(26)}
    count = 27
    
    while True:
        if words.get(msg) != None:
            result.append(words[msg])
            break
        
        for i in range(1, len(msg)+1):
            if words.get(msg[0:i]) == None:
                result.append(words[msg[0:i-1]])
                words[msg[0:i]] = count
                count += 1
                msg = msg[i-1:]
                break
        
    return result
        