def solution(numbers):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = numbers
    for i in range(10):
        result = result.replace(num[i], str(i))
    
    return int(result)
    