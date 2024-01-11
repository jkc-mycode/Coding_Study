def solution(A, B):
    val = A
    count = 0
    for i in range(len(A)):
        if val == B:
            return count
        val = val[len(val)-1] + val[0:len(val)-1]
        count += 1
        
    return -1
        