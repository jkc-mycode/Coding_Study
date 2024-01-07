def solution(sides):
    count = 0
    for i in range(1, sides[0] + sides[1] + 1):
        num = [sides[0], sides[1], i]
        if sum(num) - max(num) * 2 > 0:
            count += 1
    return count