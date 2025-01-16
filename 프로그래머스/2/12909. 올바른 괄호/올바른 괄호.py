def solution(s):
    if s[0] == ')':
        return False
    
    s_stack = []
    for i in s:
        if i == '(':
            s_stack.append(1)
        elif i == ')' and len(s_stack) != 0:
            s_stack.pop()
    
    return (True if len(s_stack) == 0 else False)