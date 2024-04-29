function solution(n) {
    let result = [];
    result = ("" + n).split("").reverse().map((item) => {
        return item - 0
    })
    return result;
}