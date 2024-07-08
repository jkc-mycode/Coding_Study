function solution(clothes) {
    let result = 0;
    const obj = {};
    
    for (let val of clothes) {
        if (!obj[val[1]]) {
            obj[val[1]] = [val[0]];
        } else {
            obj[val[1]].push(val[0]);
        }
    }
    
    for (const key in obj) {
        if (result === 0) {
            result = obj[key].length + 1;
        } else {
            result *= obj[key].length + 1;
        }
    }
    
    return result - 1;
}