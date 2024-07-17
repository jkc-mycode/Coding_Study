function solution(word) {
    const alpha = ['A', 'E', 'I', 'O', 'U'];
    let count = 0;
    let isWord = false;
    
    function dfs(val) {
        if (val.length > 5 || isWord) return;
        
        count++;
        if (val === word) {
            console.log("정답");
            isWord = true;
            return;
        }
        
        for (let i = 0; i < alpha.length; i++) {
            dfs(val + alpha[i]);
        }
    }
    
    for(let i = 0; i < alpha.length; i++) {
        dfs(alpha[i]);
    }
    
    return count;
}