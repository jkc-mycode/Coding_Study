function solution(ingredient) {
    let result = 0;
    let temp = [];
    
    for (let i = 0; i < ingredient.length; i++) {
        temp.push(ingredient[i]);
        
        if (temp.length >= 4) {
            if (temp.slice(-4).join('') === '1231') {
                result++;
                temp.pop();
                temp.pop();
                temp.pop();
                temp.pop();
            }
        }
    }
    return result;
}