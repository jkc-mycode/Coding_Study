def solution(numbers):
    result = []
    for num in numbers:
        result.append(((num ^ (num+1)) >> 2) + num + 1)
    return result