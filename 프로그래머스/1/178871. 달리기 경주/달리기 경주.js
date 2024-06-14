function solution(players, callings) {
    let obj = {};
    players.forEach((val, index) => {
        obj[val] = index;
    })
    
    let temp, index;
    for (let val of callings) {
        index = obj[val]
        temp = players[index-1];
        
        players[index-1] = val;
        players[index] = temp;
        
        obj[val] -= 1;
        obj[temp] += 1
    }
    return players;
}