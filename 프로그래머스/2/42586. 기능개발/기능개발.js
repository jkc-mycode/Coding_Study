function solution(progresses, speeds) {
    const dates = new Array(speeds.length);
    for (let i = 0; i < speeds.length; i++) {
        dates[i] = Math.ceil((100 - progresses[i]) / speeds[i]);
    }
    
    console.log(dates);
    
    const result = [];
    let max = dates[0];
    let count = 0;
    let i;
    for (i = 0; i < dates.length; i++) {
        if (dates[i] <= max) {
            count++;
        } else {
            result.push(count);
            max = dates[i];
            i--;
            count = 0;
        }
    }
    result.push(count);
    
    return result;
}