def solution(s):
    result = [0, 0]
    
    while s != "1":
        result[1] += s.count("0")
        s = s.replace("0", "")
        result[0] += 1
        s = bin(len(s))[2:]

    return result