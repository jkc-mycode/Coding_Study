def is_right(s):
    s_dict = {'(': ')', '[': ']', '{': '}'}
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if s_dict.get(stack[-1]) and s_dict[stack[-1]] == i:
                stack.pop()
            else:
                stack.append(i)
    
    if len(stack) == 0:
        return True
    else:
        return False

def solution(s):
    result = 0
    for i in range(len(s)):
        new_s = s[i:] + s[:i]
        if is_right(new_s):
            result += 1
    
    return result