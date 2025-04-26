function solution(s){
    const stack = []
    
    Array.from(s).forEach((str) => {
        if (stack[stack.length-1] === '(' && str === ')') {
            stack.pop();
        } else {
            stack.push(str)
        }
    });

    return stack.length === 0;
}