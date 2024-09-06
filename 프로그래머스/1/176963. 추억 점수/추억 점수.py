def solution(name, yearning, photo):
    result = []
    for val in photo:
        count = 0
        for i in range(len(val)):
            if val[i] in name:
                count += yearning[name.index(val[i])]
        result.append(count)
    
    return result