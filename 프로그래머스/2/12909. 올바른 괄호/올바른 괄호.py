def solution(s):
    stack = []
    if s[0] == ')': return False
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif stack:
            stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False