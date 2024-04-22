function solution(s){
    let p = 0;
    let y = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === 'p' || s[i] === 'P') {
            p++;
        } else if (s[i] === 'y' || s[i] === 'Y') {
            y++;
        }
    }
    console.log(p, y);
    
    if(p === y) {
        return true
    } else {
        return false
    }

}