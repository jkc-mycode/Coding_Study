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
        const temp = [];
        for (let str of arr) {
            if (str === '(' || str === '{' || str === '[') stack.push(str);
            else {
                if (stack.length && stack[stack.length-1] === obj[str]) stack.pop();
                else temp.push(str);
            }
        }
        
        if (!stack.length && !temp.length) result++;
    }
    return result;
}