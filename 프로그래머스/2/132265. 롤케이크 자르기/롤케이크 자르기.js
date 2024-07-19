function solution(topping) {
    let result = 0;
    let cakeA = {};
    let cakeACount = 0; // cakeA의 토핑의 수
    let cakeB = new Set();
    
    // cakeA에 모든 토핑을 옮김
    for(let i = 0; i < topping.length; i++) {
        if (cakeA[topping[i]]) {
            cakeA[topping[i]]++;
        } else {
            cakeA[topping[i]] = 1;
            cakeACount++;
        }
    }
    
    // 하나씩 cakeB로 옮기면서 토핑의 개수 확인
    for(let i = 0; i < topping.length; i++) {
        cakeB.add(topping[i]);
        cakeA[topping[i]]--;
        
        if (!cakeA[topping[i]]) cakeACount--;
        
        if (cakeACount === cakeB.size) result++;
    }
    
    return result;
}