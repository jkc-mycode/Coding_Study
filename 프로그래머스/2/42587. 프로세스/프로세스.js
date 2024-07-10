function solution(priorities, location) {
    const test = [];
    for (let i = 0; i < priorities.length; i++) {
        test.push([i, priorities[i]]);
    }
    
    let count = 0;
    
    while(true) {
        const max = test.reduce((a, b) => a[1] > b[1] ? a : b)[1];
        
        let shift;
        if (test[0][1] < max) {
            const temp = test.shift();
            test.push(temp);
        } else if (test[0][1] === max) {
            count++;
            shift = test.shift();
        }
        
        if (shift && shift[0] === location) {
            break;
        }
    }
     return count;
}