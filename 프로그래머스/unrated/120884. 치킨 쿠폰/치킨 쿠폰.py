def solution(chicken):
    n = chicken
    val = 0
    coupon = 0
    while n > 1:
        print(val, n)
        val += n/10
        n /= 10
        
    return int(val)