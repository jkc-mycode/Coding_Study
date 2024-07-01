function solution(elements) {
    let result = [];
    const length = elements.length;
    
    for (let i = 1; i < length; i++) {
        for (let j = 0; j <length; j++) {
            let temp = 0
            for (let k = j; k < j+i; k++) {
                temp += elements[k % length];
            }
            result.push(temp);
        }
    }
    
    const last = elements.reduce((acc, cur) => {
        return acc + cur
    }, 0);
    result.push(last);
    
    const set = new Set(result);
    return [...set].length;
}