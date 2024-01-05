def solution(order):
    return sum([1 for i in str(order) if '3'==i or '6'==i or '9'==i])