def solution(food):
    for i in range(1, len(food)):
        if (food[i] % 2 != 0):
            food[i] -= 1
    
    result = ''
    for i in range(1, len(food)):
        result += (str(i) * int(food[i] / 2))
    
    return result + '0' + "".join(reversed(list(result)))