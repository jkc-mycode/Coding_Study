import math
from itertools import permutations

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    result = 0
    numbers = list(numbers)
    permutation_list = []
    for i in range(1, len(numbers)+1):
        permutation_list += ["".join(list(n)) for n in permutations(numbers, i)]
    
    permutation_list = list(set(list(map(int, permutation_list))))
    
    for num in permutation_list:
        if isPrime(num):
            result += 1
    return result