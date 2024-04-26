function solution(n) {
    let result = n;
    
    for (let i = 1; i <= n/2; i++){
        if (n % i === 0) {
            result += i;
        }
    }
    
    return result;
}