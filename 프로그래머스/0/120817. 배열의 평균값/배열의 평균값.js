function solution(numbers) {
    let result = 0;
    numbers.forEach((value) => {
        result += value;
    });
    
    return result / numbers.length;
}