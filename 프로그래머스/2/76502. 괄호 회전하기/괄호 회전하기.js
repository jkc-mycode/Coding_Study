function solution(s) {
    let result = 0;
    let arr = s.split('');
    
    const obj = {
        ')': '(', 
        '}': '{', 
        ']': '['
    };
    
    for (let i = 0; i < arr.length; i++) {
        if (i) arr.push(arr.shift());
        
        const stack = [];
        const queue = [];
        for (let str of arr) {
            if (str === '(' || str === '{' || str === '[') stack.push(str);
            else {
                if (stack.length && stack[stack.length-1] === obj[str]) stack.pop();
                else queue.push(str);
            }
        }
        
        if (!stack.length && !queue.length) result++;
    }
    return result;
}