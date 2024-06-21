function solution(brown, yellow) {
    let width = brown / 2;
    let height = 2;
    let area = brown + yellow;
    
    while (true) {
        if (area === (width * height)) break;
        width--;
        height++;
    }
    
    return [width, height];
}