def solution(s):
    value = 0
    pre_value = 0
    for i in s.split(" "):
        if i.isdigit() or i[0]=='-':
            value += int(i)
            pre_value = int(i)
        else:
            value -= pre_value
    return value