function solution(want, number, discount) {
    let result = 0;
    for (let i = 0; i < discount.length - 9; i++) {
        let j;
        for (j = 0; j < want.length; j++) {
            let count = 0;
            for (let k = i; k < i + 10; k++) {
                if (discount[k] === want[j]) count ++;
            }
            if (count < number[j]) break;
        }
        if (j === want.length) result++;
    }
    return result;
}