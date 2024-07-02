function solution(citations) {
    let use;
    let max = -99;
    for (let i = 0; i <= Math.max(...citations); i++) {
        use = citations.filter((val) => val >= i);
        
        if (use.length >= i) {
            max = i;
        } else {
            break;
        }
    }
    return max;
}