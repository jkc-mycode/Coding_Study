def solution(msg):
    result = []
    index = 26
    dictionary = {chr(64+i): i  for i in range(1, 27)}
    
    i = 0
    while i < len(msg):
        j = 1
        while i+j <= len(msg) and msg[i:i+j] in dictionary:
            j += 1
        
        result.append(dictionary.get(msg[i:i+j-1]))
        if i+j <= len(msg):
            index += 1
            dictionary[msg[i:i+j]] = index
        i += j - 1
            
    
    return result