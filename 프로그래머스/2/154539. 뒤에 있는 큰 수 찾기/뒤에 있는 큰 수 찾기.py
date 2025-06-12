def solution(numbers):
    result = [-1] * len(numbers)
    stack = []
    
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            index = stack.pop()
            result[index] = num
        stack.append(i)
    
    return result
            
    
    