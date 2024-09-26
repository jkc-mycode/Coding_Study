# 결과 리스트 순서가 상관 없을 때
# def solution(arr):
#     arr.sort(reverse=True)
#     arr = arr[:-1]
#     if len(arr) == 0:
#         return [-1]
#     else:
#         return arr

# 결과 리스트 순서가 상관 있을 때
def solution(arr):
    min = 9999
    for i in arr:
        if min > i:
            min = i

    arr.remove(min)
    if len(arr) == 0:
        return [-1]
    else:
        return arr

print(solution([4,3,2,1]))
print(solution([10]))
