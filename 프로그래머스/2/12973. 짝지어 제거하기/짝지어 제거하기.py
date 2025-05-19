def solution(s):
    stack = [s[0]]
    i = 1
    while i < len(s):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
        i += 1
        
    if len(stack) == 0:
        return 1
    else:
        return 0
    