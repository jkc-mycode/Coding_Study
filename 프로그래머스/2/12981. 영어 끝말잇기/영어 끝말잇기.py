import math

def solution(n, words):
    words_dict = {words[0]: 1}
    result = [0, 0]
    
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words_dict.get(words[i]):
            result[0] = (i + 1) % n if (i + 1) % n != 0 else n
            result[1] = math.ceil((i + 1) / n)
            break
            
        if words_dict.get(words[i]):
            words_dict[words[i]] += 1
        else:
            words_dict[words[i]] = 1
    
    return result