function solution(food) {
    for (let i = 1; i < food.length; i++) {
        if (food[i] % 2 !== 0) {
            food[i] -= 1;
        }
    }
    
    let result = '';
    for (let i = 1; i < food.length; i++) {
        result += String(i).repeat(food[i] / 2);
    }
    return result + "0" + result.split("").reverse().join("");
}