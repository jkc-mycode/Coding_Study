function solution(s) {
    s = s.toLowerCase();
    let strArr = s.split(" ");
    
    for (let i = 0; i < strArr.length; i++) {
        if (!isNaN(strArr[i][0])) continue;
        
        strArr[i] = strArr[i].split("");
        // 공백이 연속일 때는 strArr[i]의 길이는 0
        if (strArr[i].length !== 0)
            // 공백은 toUpperCase()를 못하기 때문에 런타임에러 발생
            strArr[i][0] = strArr[i][0].toUpperCase();
        strArr[i] = strArr[i].join("");
    }
    return strArr.join(" ")
}