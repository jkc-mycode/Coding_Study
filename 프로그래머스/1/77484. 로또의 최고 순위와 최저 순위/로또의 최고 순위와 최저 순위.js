function solution(lottos, win_nums) {
    const rank = { 6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6 };
    let win_count = 0;
    let zero_count = 0;
    
    for (let i of lottos) {
        if (win_nums.includes(i)) {
            win_count++;
        } else if (i === 0) {
            zero_count++;
        }
    }
    return [rank[win_count + zero_count], rank[win_count]];
}