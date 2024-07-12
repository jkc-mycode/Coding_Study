function solution(numbers, target) {
    let result = 0;
    
    function dfs(index, cal) {
        if (index === numbers.length) {
            if(cal === target) {
                result++;
            }
            return;
        }
        
        dfs(index + 1, cal + numbers[index]);
        dfs(index + 1, cal - numbers[index]);
    }
    
    dfs(0, 0);
    
    return result;
}