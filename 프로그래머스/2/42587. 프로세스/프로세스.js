function solution(priorities, location) {
    const queue = [];
    for (let i = 0; i < priorities.length; i++) {
        queue.push([i, priorities[i]]);
    }
    
    let count = 0;
    
    while(true) {
        const max = queue.reduce((a, b) => a[1] > b[1] ? a : b)[1];
        
        let shift;
        if (queue[0][1] < max) {
            queue.push(queue.shift());
        } else if (queue[0][1] === max) {
            count++;
            shift = queue.shift();
        }
        
        if (shift && shift[0] === location) {
            break;
        }
    }
     return count;
}