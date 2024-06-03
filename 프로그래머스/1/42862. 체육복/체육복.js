function solution(n, lost, reserve) {  
    let lostTemp = lost.filter((a) => !reserve.includes(a)).sort((a, b) => a - b);
    let reserveTemp = reserve.filter((a) => !lost.includes(a)).sort((a, b) => a - b);
    
    let result =  n - lostTemp.length;
    
    for (let i = 0; i < lostTemp.length; i++) {
        for (let j = 0; j < reserveTemp.length; j++) {
            if (reserveTemp[j] - 1 === lostTemp[i] || reserveTemp[j] + 1 === lostTemp[i]) {
                result++;
                reserveTemp[j] = 0;
                break;
            }
        }
    }
    return result;
}