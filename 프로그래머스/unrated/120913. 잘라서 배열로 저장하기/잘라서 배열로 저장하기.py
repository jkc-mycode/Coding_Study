def solution(my_str, n):
    value = []
    for i in range(len(my_str) // n+1):
        value.append(my_str[n*i:(i+1)*n])
    if len(my_str) % n == 0:
        value.pop()
    return value