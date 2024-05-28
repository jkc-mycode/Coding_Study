function solution(n, m, section) {
    const arr = new Array(n).fill(1);
    
    for (let i of section) {
        arr[i-1] = 0;
    }
    
    let result = 0;
    for (let i = 0; i < n; i++) {
        if (arr[i] === 0) {
            result++;
            for (let j = 0; j < m; j++) {
                if (i + j > n - 1) {
                    break;
                }
                arr[i+j] = 1;
            }
        }
    }
    return result;
}