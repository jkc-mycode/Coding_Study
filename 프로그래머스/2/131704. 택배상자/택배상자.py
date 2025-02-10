def solution(order):
    result = 0
    stack = []
    current = 1

    for o in order:
        while current <= len(order) and current < o:
            stack.append(current)
            current += 1
            
        if current == o:
            result += 1
            current += 1
        elif stack and stack[-1] == o:
            stack.pop()
            result += 1
        else:
            break

    return result