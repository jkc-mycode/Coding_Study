def solution(s):
    result = sorted(list(map(int, s.split(" "))))
    return str(result[0]) + " " + str(result[-1])