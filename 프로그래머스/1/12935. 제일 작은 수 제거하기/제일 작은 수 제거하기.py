def solution(arr):
    result = []
    min_value = min(arr)
    for i in arr:
        if min_value != i:
            result.append(i)

    if len(result) == 0:
        return [-1]
    else:
        return result