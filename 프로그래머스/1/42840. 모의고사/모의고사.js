function solution(answers) {
    const std1 = [1, 2, 3, 4, 5];
    const std2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    const score = [0, 0, 0];
    let result = [];
    
    for (let i = 0; i < answers.length; i++) {
        if (answers[i] === std1[i % std1.length]) {
            score[0]++;
        }
        if (answers[i] === std2[i % std2.length]) {
            score[1]++;
        }
        if (answers[i] === std3[i % std3.length]) {
            score[2]++;
        }
    }
    for (let i = 0; i < 3; i++) {
        if (Math.max(...score) <= score[i]) {
            result.push(i + 1);
        }
    }
    return result;
}