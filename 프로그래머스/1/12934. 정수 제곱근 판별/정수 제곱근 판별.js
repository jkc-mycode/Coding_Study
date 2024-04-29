function solution(n) {
    let temp = Math.pow(n, 0.5);
    if (Number.isInteger(temp)) {
        return Math.pow(temp+1, 2);
    } else {
        return -1
    }
}