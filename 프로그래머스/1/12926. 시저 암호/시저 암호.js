function solution(s, n) {
    let result = '';
    for (let i = 0; i < s.length; i++) {
        let code = s[i].charCodeAt();
        if (code <= 90 && code >= 65) {
            if (code + n > 90) {
                result += String.fromCharCode(code + n - 26);
            } else {
                result += String.fromCharCode(code + n);
            }
        } 
        else if (code <= 122 && code >= 97) {
            if (code + n > 122) {
                result += String.fromCharCode(code + n - 26);
            } else {
                result += String.fromCharCode(code + n);
            }
        } 
        else if (s[i] === ' ') {
            result += ' ';
        }
    }
    return result;
}