function solution(t, p) {
    let result = 0;
    
    for (let i = 0; i < t.length; i++) {
        if (t.slice(i, i + p.length).length === p.length) {
            if (Number(t.slice(i, i + p.length)) <= Number(p)) {
                result++;
            }
        }
    }
    return result;
}