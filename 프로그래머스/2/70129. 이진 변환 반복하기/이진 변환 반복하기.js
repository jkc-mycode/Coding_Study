function solution(s) {
    let binary = '';
    let binaryCount = 0;
    let zeroCount = 0;
    
    while(s !== '1') {
        for (let val of s) {
            val.split('').forEach((a) => { 
                 a === '1' ?  binary += a : zeroCount++ 
            })
        }
        binaryCount++;
        s = binary.length.toString(2);
        binary = '';
    }
    return [binaryCount, zeroCount]
}