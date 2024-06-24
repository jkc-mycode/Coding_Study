function solution(n,a,b)
{
    let round = 0;
    while (true) {
        a = Math.round(a/2);
        b = Math.round(b/2);
        round++;
        if (a === b){
            return round;
        }
    }
}