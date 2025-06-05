def solution(numbers, target):
    result = 0
    def dfs(index, cur_sum):
        nonlocal result
        if index == len(numbers):
            if cur_sum == target:
                result += 1
            return 
        
        dfs(index + 1, cur_sum + numbers[index])
        dfs(index + 1, cur_sum - numbers[index])
    
    dfs(0, 0)
    return result