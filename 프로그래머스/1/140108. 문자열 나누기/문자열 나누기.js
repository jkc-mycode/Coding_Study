function solution(s) {
    const result = [];
    let len = s.length;
    let temp = s;
    let same = 0;
    let diff = 0;
    
    for (let i = 0; i < len; i++) {
        if (s[0] == temp[i]) {
            same++;
        } else {
            diff++;
        }
        
        if (same === diff) {
            result.push(s.slice(0, same+diff));
            s = temp.slice(i+1, temp.length);
            same = 0;
            diff = 0;
        }
    }
    if (s !== '') {
        result.push(s);
    }
    
    return result.length
}