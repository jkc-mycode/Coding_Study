def solution(s):
    result = sorted(s.split(' '), key=lambda x: int(x))
    return result[0] + ' ' + result[-1]