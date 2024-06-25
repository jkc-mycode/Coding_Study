function gcd(a, b) {
    if (b <= 0)
        return a;
    
    return gcd(b, a % b);
}

function lcm(a, b) {
    return a * b / gcd(a, b);
}

function solution(arr) {
    let result;
    if (arr.length === 1) {
        return arr[0];
    } else if (arr.length === 2) {
        return lcm (arr[0], arr[1]);
    } else {
        result = lcm (arr[0], arr[1]);
        
        for (let i = 2; i < arr.length; i++) {
            result = lcm(result, arr[i]);
        }
        
    }
    return result;
}