def solution(my_string):
    s = my_string.split(" ")
    value = int(s[0])
    o = 1
    for i in range(1, len(s)):
        if s[i] == "+":
            o *= o
        elif s[i] == "-":
            o = -(o**2)
        else:
            value += int(s[i])*o

    return value
            
            
        