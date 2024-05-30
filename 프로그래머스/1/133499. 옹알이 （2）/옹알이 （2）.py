def solution(babbling):
    nephew = ["aya", "ye", "woo", "ma"]
    result = 0
    
    for i in range(len(babbling)):
        for j in range(len(nephew)):
            if nephew[j] + nephew[j] in babbling[i]:
                break;
            babbling[i] = babbling[i].replace(nephew[j], ' ')
        if babbling[i].replace(' ', '') == '':
            result += 1
    return result