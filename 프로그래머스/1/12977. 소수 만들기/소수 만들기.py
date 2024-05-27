def solution(nums):
    result = 0
    temp = 0
    is_prime = True
    
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                temp = nums[i] + nums[j] + nums[k]
                is_prime = True
                for l in range(2, int(temp / 2)):
                    if temp % l == 0: is_prime = False
                if is_prime: result += 1
    return result