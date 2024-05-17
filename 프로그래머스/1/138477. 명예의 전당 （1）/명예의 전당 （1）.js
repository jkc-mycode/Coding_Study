function solution(k, score) {
    const result = [];
    const topK = [];
    
    for (let i = 0; i < score.length; i++) {
        topK.push(score[i]);
        topK.sort((a, b) => b - a);
        if (topK.length > k) {
            topK.pop();
        }
        result.push(topK.at(-1));
    }
    return result;
}