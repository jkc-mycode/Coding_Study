def solution(n, arr1, arr2):
    result = []
    for i in range(n):
        temp = bin(arr1[i] | arr2[i])[2:].zfill(n)
        temp = temp.replace("1", "#")
        temp = temp.replace("0", " ")
        result.append(temp)
    
    return result
        