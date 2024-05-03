function solution(left, right) {
    let result = 0;
    let count;
    for (let i = left; i <= right; i++) {
        count = 1;
        for (let j = 1; j <= Math.round(i / 2); j++) {
            if (i % j === 0) {
                count++;
            }
        }
        
        if (i === 1) count = 1;
        
        if (count % 2 === 0) {
            result += i;
        } else {
            result -= i;
        }
    }
    return result;
}