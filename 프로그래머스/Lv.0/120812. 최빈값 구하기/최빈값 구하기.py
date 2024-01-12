def solution(array):
    val = list(set(array))

    count_list = [array.count(i) for i in val]
    max_val = max(count_list)
    
    if count_list.count(max_val) == 1:
        temp = val[count_list.index(max_val)]
        return array[array.index(temp)]
    else:
        return  -1