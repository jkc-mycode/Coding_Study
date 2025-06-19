result = 0
def dfs(index, num_sum, numbers, target):
    global result
    if index == len(numbers) and num_sum == target:
        result += 1
        return 
    if index == len(numbers):
        return
    
    dfs(index + 1, num_sum + numbers[index], numbers, target)
    dfs(index + 1, num_sum - numbers[index], numbers, target)

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return result