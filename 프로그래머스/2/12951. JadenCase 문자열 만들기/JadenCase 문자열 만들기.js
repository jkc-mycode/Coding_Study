function solution(s) {
    s = s.toLowerCase();
    let strArr = s.split(" ");
    
    for (let i = 0; i < strArr.length; i++) {
        if (!isNaN(strArr[i][0])) continue;
        
        strArr[i] = strArr[i].split("");
        if (strArr[i].length !== 0)
            strArr[i][0] = strArr[i][0].toUpperCase();
        strArr[i] = strArr[i].join("");
    }
    return strArr.join(" ")
}