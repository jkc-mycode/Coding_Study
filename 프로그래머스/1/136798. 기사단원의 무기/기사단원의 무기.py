def getDivisorCount(num):
    if num == 1: return 1

    count = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            count += 1
            if (num / i != i): count += 1
    return count

def solution(number, limit, power):
    arr = []
    for i in range(1, number+1):
        if getDivisorCount(i) > limit:
            arr.append(power)
        else:
            arr.append(getDivisorCount(i))
    
    return sum(arr)