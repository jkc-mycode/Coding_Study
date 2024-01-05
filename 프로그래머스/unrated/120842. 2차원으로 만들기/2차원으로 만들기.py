def solution(num_list, n):
    result = []
    for i in range(len(num_list)//n):
        result.append([j for j in num_list[i*n:(i+1)*n]])
        
    return result