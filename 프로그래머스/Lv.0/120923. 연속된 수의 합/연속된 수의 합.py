def solution(num, total):
    val = [i for i in range(-total-100, total+100)]
    for i in range(len(val)-2):
        if total == sum(val[i:i+num]):
            return val[i:i+num]