function solution(babbling) {
    const nephew = ["aya", "ye", "woo", "ma"];
    let result = 0;
    
    for (let i in babbling) {
        for (let j in nephew) {
            if (babbling[i].includes(nephew[j] + nephew[j])) break;
            babbling[i] = babbling[i].replaceAll(nephew[j], ' ');
        }
        
        if (babbling[i].replaceAll(' ', '') === '') {
            result++;
        }
    }
    return result;
}