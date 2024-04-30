function solution(x) {
    let temp = (x.toString().split("")).map((item) => item - 0);
    let sum = temp.reduce((a, b) => a + b, 0);
    
    if (x % sum === 0) return true;
    else return false;
}