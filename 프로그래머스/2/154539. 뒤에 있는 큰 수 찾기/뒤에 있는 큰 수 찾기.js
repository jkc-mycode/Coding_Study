function solution(numbers) {
    const result = new Array(numbers.length).fill(-1);
    
    for(let i = numbers.length-2; i >= 0; i--) {
        for(let j = i+1; j < numbers.length; j++) {
            if (numbers[i] < numbers[j]) {
                result[i] = numbers[j];
                break;
            } else {
                if (result[j] === -1) {
                    result[i] = -1;
                    break;
                } else if (numbers[i] < result[j]) {
                    result[i] = result[j];
                    break;
                }
            }
        }
    }
    
    return result;
}