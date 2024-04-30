function solution(n) {
    let result = Number(n.toString().split("").sort((a, b) => b - a).join(""));
    return result;
}