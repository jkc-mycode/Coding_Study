function solution(array, commands) {
    let val;
    let result = [];
    for (let i = 0; i < commands.length; i++) {
        val = array.slice(commands[i][0] - 1, commands[i][1]);
        val.sort((a, b) => a - b);
        result.push(val[commands[i][2] - 1]);
    }
    return result;
}