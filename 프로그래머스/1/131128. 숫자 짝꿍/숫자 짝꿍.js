function solution(X, Y) {
    let result = '';
    
    const arrX = X.split('');
    const arrY = Y.split('');
    
    for (let i = 9; i > -1; i--) {
        let countX = arrX.filter((a) => Number(a) === i).length;
        let countY = arrY.filter((a) => Number(a) === i).length;
        
        result += String(i).repeat(Math.min(countX, countY));
    }
    
    if (result === '') return '-1';
    if (result[0] === '0') return '0';
    
    return result;
   
}