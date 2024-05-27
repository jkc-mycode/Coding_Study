function solution(nums) {
    let result = 0;
    let isPrime = true;
    
    for (let i = 0; i < nums.length - 2; i++) {
        for (let j = i + 1; j < nums.length - 1; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                isPrime = true;
                for (let l = 2; l < nums[i] + nums[j] + nums[k]; l++) {
                    if ((nums[i] + nums[j] + nums[k]) % l === 0)
                        isPrime = false;
                }
                if (isPrime){
                    result++;
                }
            }
        }
    }
    return result;
}