def solution(n):
    for i in range(0, n*6+1, n):
        if i%6==0 and i!=0:
            return i//6
        
            