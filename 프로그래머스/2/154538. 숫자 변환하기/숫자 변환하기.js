function solution(x, y, n) {
    function cal(cur, num) {
        switch(num) {
            case 0: 
                return cur-n;
            case 1:
                if (cur % 2 === 0) {
                    return cur/2;
                } else {
                    return 0;
                }
            case 2:
                if (cur % 3 === 0) {
                    return cur/3;
                } else {
                    return 0;
                }
        }
    }
    
    function bfs() {
        const queue = [[y, 0]];
        const visited = {};
        visited[y] = 1;
        
        while (queue.length !== 0) {
            const [cur, count] = queue.shift();
            
            if (cur === x) return count;
            
            for (let i = 0; i < 3; i++) {
                let value = cal(cur, i);
                
                if (value >= x && !visited[value]) {
                    visited[value] = 1;
                    queue.push([value, count+1]);
                }
            }
        }
        return -1;
    }
    return bfs();
}