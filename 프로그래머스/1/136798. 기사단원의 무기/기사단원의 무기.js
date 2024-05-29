function getDivisorCount(num) {
    if (num === 1) return 1;
    
    let count = 0;
    for (let i = 1; i <= Math.sqrt(num); i++) {
        if (num % i === 0){
            count++;
            if (num / i !== i) count++;
        }
    }
    return count;
}

function solution(number, limit, power) {
    const arr = [];
    for (let i = 1; i < number + 1; i++){
        arr.push(getDivisorCount(i));
    }
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > limit) {
            arr[i] = power
        }
    }
    return arr.reduce((a, b) => a + b);
}