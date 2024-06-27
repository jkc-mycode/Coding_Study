function solution(k, tangerine) {
    const counts = tangerine.reduce((acc, cur) => {
        acc.set(cur, (acc.get(cur) || 0) + 1);
        return acc;
    }, new Map());
    
    const countsArr = [...counts.values()].sort((a, b) => b-a);
    let result = 0;
    
    for (let count of countsArr) {
        if (k >= count) {
            k -= count;
            result++;
        } else if (k > 0) {
            result++;
            break;
        } else {
            break;
        }
    }
    
    return result;
}