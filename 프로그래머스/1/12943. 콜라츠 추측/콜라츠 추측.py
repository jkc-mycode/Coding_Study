def solution(num):
    if num == 1: return 0
    
    number = num
    count = 0
    while(1):
        if count >= 500: return -1
        
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        count += 1
        
        if number == 1: return count
    