def solution(keymap, targets):
    result = []
    
    for target in targets:
        count = 0
        for j in target:
            min = 99999
            for key in keymap:
                if (key.find(j) != -1 and key.find(j) < min):
                    min = key.find(j)
            count += min + 1
        if count > 9999:
            result.append(-1)
        else:
            result.append(count)
    return result