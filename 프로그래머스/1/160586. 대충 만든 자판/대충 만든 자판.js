function solution(keymap, targets) {
    let result = [];
    let count;
    
    for (let i = 0; i < targets.length; i++) {
        count = 0;
        for (let j = 0; j < targets[i].length; j++) {
            let keyIndex = keymap.map((key) => {
                if (key.indexOf(targets[i][j]) === -1) {
                    return 99999;
                } else {
                    return key.indexOf(targets[i][j]);
                }
            })
            // console.log(targets[i][j], keyIndex);
            count += Math.min(...keyIndex) + 1;
        }
        if (count > 99999) {
            result.push(-1);
        } else {
            result.push(count);
        }
    }
    return result;
}