function solution(park, routes) {
    let start = [];
    
    // 시작점 찾기
    for (let i = 0; i < park.length; i++) {
        if (park[i].indexOf("S") !== -1) {
            start.push(i);
            start.push(park[i].indexOf("S"));
        }
    }
    
    // 방향에 따른 이동
    const direction = {
        N: [-1, 0],
        S: [1, 0],
        W: [0, -1],
        E: [0, 1]
    }
    
    for (let route of routes) {
        // 방향과 거리로 나눔
        const [dir, dist] = route.split(" ");
        
        let [x, y] = start
        
        // 한 걸음씩 증가시키기 위한 변수
        let temp = 0;
        while (temp < dist) {
            // 시작점과 이동 방향에 따른 이동을 더함
            x += direction[dir][0];
            y += direction[dir][1];
            
            //밖에 나가거나 장애물을 만날 경우
            if (x < 0 || x >= park.length || y < 0 || y >= park[0].length || park[x][y] === "X") {
                break;
            }
            temp++;
        }
        // dist 만큼 이동이 완료되면 (밖에 나가거나 장애물을 만나지 않음)
        if (+dist === temp) {
            start = [x, y];
        }
    }
    return start
}