def solution(numer1, denom1, numer2, denom2):
    result = [0, 0]
    #최소공배수
    for i in range(max(denom1, denom2), denom1*denom2+1):
        if i%denom1==0 and i%denom2==0:
            result[1] = i
            break
    result[0] = int(numer1*(result[1]/denom1) + numer2*(result[1]/denom2))
    #최대공약수
    for i in range(min(result[0], result[1]), 0, -1):
        if result[0]%i==0 and result[1]%i==0:
            result[0] = int(result[0]/i)
            result[1] = int(result[1]/i)

    return result