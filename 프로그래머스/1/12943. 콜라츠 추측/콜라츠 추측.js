function solution(num) {
    if (num === 1) return 0;
    
    let number = num;
    let count = 0;
    
    while(true) {
        if (count >= 500) return -1;
        
        if (number % 2 === 0) {
            number /= 2;
        } else {
            number = number * 3 + 1;
        }
        count++;
        
        if (number === 1) return count;
    }
}