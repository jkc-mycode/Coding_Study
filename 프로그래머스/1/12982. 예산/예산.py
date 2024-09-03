def solution(d, budget):
    count = 0;
    d.sort()
    for i in d:
        if i <= budget:
            count += 1
            budget -= i
    return count