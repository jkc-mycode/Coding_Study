function solution(arr) {
    let min = Math.min(...arr);
    let result = arr.filter((item) => { return item !== min; })
    
    if (result.length == 0) {
        return [-1];
    } else {
        return result;
    }
}