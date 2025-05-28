def solution(s):
    result = []
    s_list = list(set(i.split(',')) for i in s[2:-2].split('},{'))
    s_list = sorted(s_list, key=lambda x: len(x))
    
    temp = set()
    for i in s_list:
        result += list(map(int, i - temp))
        temp = i | temp
    
    return result