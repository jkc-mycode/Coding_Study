function solution(k, dungeons) {
    const result = []; // 방문 횟수를 저장하기 위한 배열
    // 각 던전 방문 여부를 체크를 위한 배열
    const visited = new Array(dungeons.length).fill(false); 
    
    // 완전 탐색을 위한 DFS(진행 횟수, 체력)
    function dfs(count, hp) {
        // 현재 dfs의 진행 횟수 저장
        result.push(count);
        
        // 던전의 수 만큼 반복 
        // 즉, dungeons[0]을 처음으로 갔을 때, dungeons[1]을 처음으로 갔을 때 등등
        for (let i = 0; i < dungeons.length; i++) {
            // 방문하지 않았고 던전에 들어갈 체력이 있을 때
            if (!visited[i] && dungeons[i][0] <= hp) {
                visited[i] = true; // 방문했다는 의미로 체크
                dfs(count + 1, hp - dungeons[i][1]); // 다음 던전으로 진입
                //매 for문마다 다른 노드들이 전부 false인 상태로 작업을 할 수 있게 됨
                visited[i] = false;
            }
        }
    }
    
    dfs(0, k);
    
    return Math.max(...result);
}
