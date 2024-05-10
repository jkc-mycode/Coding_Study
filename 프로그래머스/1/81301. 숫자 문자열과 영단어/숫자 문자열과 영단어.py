def solution(s):
    alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    result = ''
    temp = ''
    
    for val in s:
        if val in num:
            result += val
        else:
            temp += val
            if temp in alp:
                result += str(alp.index(temp))
                temp = ''
                
    return int(result)