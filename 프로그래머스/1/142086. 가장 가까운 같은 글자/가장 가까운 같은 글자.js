function solution(s) {
    let result = [];
    let temp = [];
    for (let i = 0; i < s.length; i++) {
        if (!temp.includes(s[i])) {
            temp.push(s[i]);
            result.push(-1);
        } else {
            let min = 9999;
            for (let j = i - 1; j >= 0; j--) {
                if (s[i] === s[j]) {
                    if ((i - j) < min) {
                        min = i - j;
                    }
                    temp.push(s[i]);
                    result.push(min);
                    break;
                }
            }
        }
    }
    return result;
}