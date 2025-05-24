def solution(s):
    result = 0
    dict_s = { ')': '(', ']': '[', '}': '{' }
    opened_s = ['(', '[', '{']
    closed_s = [')', ']', '}']
    
    for i in range(len(s)):
        new_s = s[i:] + s[:i]
        
        if new_s[0] in closed_s: continue
        
        stack = []
        for n in new_s:
            if len(stack) == 0 or n in opened_s:
                stack.append(n)
            elif dict_s[n] == stack[-1]:
                stack.pop()
        
        if len(stack) == 0:
            result += 1
    
    return result