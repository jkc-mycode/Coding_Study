def solution(arr1, arr2):
    result = list([0 for _ in range(len(arr2[0]))] for _ in range(len(arr1)))
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[i])):
                temp += arr1[i][k] * arr2[k][j]
            result[i][j] = temp
    
    return result