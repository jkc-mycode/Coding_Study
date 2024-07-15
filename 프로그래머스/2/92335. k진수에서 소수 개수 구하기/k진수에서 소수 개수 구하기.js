function isPimaryNumber(num) {
    if (num === '1' || num === '') return false;
    
    for (let i = 2; i <= Math.sqrt(+num); i++) {
        if (+num % i === 0) return false;
    }
    return true;
}

function solution(n, k) {
    const result = [];
    const number = n.toString(k);
    const list = number.split('0');

    for (let i = 0; i < list.length; i++) {
        if (isPimaryNumber(list[i])) {
            result.push(list[i]);
        }
    }
    return result.length;
}

