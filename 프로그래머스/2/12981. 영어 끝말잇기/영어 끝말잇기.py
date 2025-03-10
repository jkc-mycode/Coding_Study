def solution(n, words):
    result = [0, 0]
    i = 1
    words_dict = {w: 0 for w in words}
    
    while i < len(words):
        words_dict[words[i-1]] += 1
        if words[i-1][-1] != words[i][0] or words_dict[words[i]] != 0:
            result[0] = i % n
            result[1] = i // n
            break
        i += 1
    
    if result[0] != 0 or result[1] != 0:
        result[0] += 1
        result[1] += 1
    
    return result