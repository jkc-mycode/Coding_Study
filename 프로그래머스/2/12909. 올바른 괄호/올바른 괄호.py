def solution(s):
    stack = [s[0]]
    
    for i in s[1:]:
        if i == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)
        
    
    return len(stack) == 0