def solution(array, n):
    array = sorted(array)
    abs_list = [abs(i-n) for i in array]
    return array[abs_list.index(min(abs_list))]