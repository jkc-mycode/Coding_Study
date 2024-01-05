def solution(num, k):
    num_list = list(str(num))
    return num_list.index(str(k))+1 if str(k) in num_list else -1