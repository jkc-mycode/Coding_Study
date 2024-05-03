function solution(s) {
    if (!isNaN(s - 0) && (s.length === 4 || s.length === 6) && !(s.includes('e'))) {
        return true;
    } else {
        return false;
    }
}