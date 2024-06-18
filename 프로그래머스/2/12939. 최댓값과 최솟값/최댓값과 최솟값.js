function solution(s) {
    s = s.split(" ").map((val) => +val)
    const min = Math.min(...s);
    const max = Math.max(...s);
    
    return `${min} ${max}`
}