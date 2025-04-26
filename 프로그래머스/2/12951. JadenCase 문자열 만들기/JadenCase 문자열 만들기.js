function solution(s) {
    let arr = s.toLowerCase().split(' ');
    
    arr = arr.map((str) => str.charAt(0).toUpperCase() + str.slice(1));
    
    return arr.join(' ');
}