import re

def cal(num, opt):
    if opt == 'S':
        return num ** 1
    elif opt == 'D':
        return num ** 2
    elif opt == 'T':
        return num ** 3

def solution(dartResult):
    scores = []
    options = []
    
    # 점수와 보너스, 옵션을 한 번에 추출
    parts = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    
    for score, bonus, option in parts:
        scores.append(cal(int(score), bonus))
        options.append(option if option else ' ')

    result = 0
    for i in range(len(options)):
        if options[i] == '*':
            scores[i] *= 2
            if i > 0:
                scores[i-1] *= 2
        elif options[i] == '#':
            scores[i] *= -1
    
    return sum(scores)