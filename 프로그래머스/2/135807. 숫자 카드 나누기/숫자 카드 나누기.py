def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def multi_gcd(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

def array_check(array, result):
    for num in array:
        if num % result == 0:
            return False
    return True

def solution(arrayA, arrayB):
    result_a = multi_gcd(arrayA)
    result_b = multi_gcd(arrayB)
    
    if array_check(arrayA, result_b) == array_check(arrayB, result_a) == False:
        return 0
    
    
    return max(result_a, result_b)