function solution(s) {
    const alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    const num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
    
    let result = '';
    let temp = '';
    
    for (let i = 0; i < s.length; i++) {
        if (num.includes(s[i])) {
            result += s[i];
        } else {
            temp += s[i];
            if (alp.includes(temp)) {
                result += String(alp.indexOf(temp));
                temp = '';
            }
        }
    }
    return Number(result);
}