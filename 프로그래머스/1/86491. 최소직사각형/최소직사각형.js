function solution(sizes) {
    let temp = sizes;
    for (let i = 0; i < sizes.length; i++) {
        temp[i].sort((a, b) => a - b);
    }
    
    let maxW = -1;
    let maxH = -1;
    for (let i = 0; i < sizes.length; i++) {
        if (temp[i][0] > maxW) {
            maxW = temp[i][0];
        }
        if (temp[i][1] > maxH) {
            maxH = temp[i][1];
        }
    }
    
    return maxW * maxH;
}