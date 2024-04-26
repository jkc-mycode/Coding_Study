function solution(arr) {
    let result = 0;
    arr.map((item) => { result += item });
    return result / arr.length;
}