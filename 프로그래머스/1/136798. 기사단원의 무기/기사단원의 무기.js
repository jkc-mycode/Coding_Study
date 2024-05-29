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
        if (getDivisorCount(i) > limit) {
            arr.push(power);
        } else {
            arr.push(getDivisorCount(i));
        }
    }
    return arr.reduce((a, b) => a + b);
}