function solution(arr, divisor) {
    let result = arr.filter((num) => {
        if (num % divisor == 0) return num;
    })
    
    if (result.length === 0) return [-1];
    else return result.sort((a, b) => a - b);
}