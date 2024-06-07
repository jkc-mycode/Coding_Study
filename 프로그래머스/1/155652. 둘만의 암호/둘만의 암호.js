function solution(s, skip, index) {
    let result = '';
    let count;
    let code;
    
    for (let i = 0; i < s.length; i++) {
        count = 0;
        code = s[i].charCodeAt()
        for (let j = 0; j < index; j++) {
            code++;
            if (code > 122) {
                code = 97;
            }
            
            while (skip.includes(String.fromCharCode(code))) {
                code++;
                if (code > 122) {
                    code = 97;
                }
            }
        }
        result += String.fromCharCode(code)
    }
    return result;
}