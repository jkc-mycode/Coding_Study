def solution(numlist, n):
    sub = [abs(n-i) for i in numlist]
    val = [(a, b) for a, b in zip(numlist, sub)]
    
    return [k for k, v in sorted(val, key=lambda x: (x[1], -x[0]))]