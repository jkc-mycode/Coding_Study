function solution(n) {
    let result = 1000000;
    
    for (let i = 1; i < n; i++) {
        if (n % i === 1 && result > i) {
            result = i;
            break;
        }
    }
    
    return result;
}