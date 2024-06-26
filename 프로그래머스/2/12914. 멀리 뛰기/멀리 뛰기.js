function solution(n) {
    const fibo = [1, 1];
    
    if (n === 1) return 1;
    
    for (let i = 2; i <= n; i++) {
        fibo.push((fibo[i-2] + fibo[i-1]) % 1234567);
    }
    
    return fibo[n];
}