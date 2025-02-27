def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
            continue
            
        if stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
        
    return 1 if not stack else 0