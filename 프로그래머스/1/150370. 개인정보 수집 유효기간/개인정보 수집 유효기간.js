function solution(today, terms, privacies) {
    const result = [];
    // 현재 날짜 정보 분리
    let [curYear, curMonth, curDay] = today.split(".").map((val) => +val);
    // 개인정보에서 가입 날짜와 약관 종류로 분리
    privacies = privacies.map((val) => val.split(" "));
    // 약관 유효기간을 약관 종류와 유효기간으로 분리
    terms = terms.map((val) => val.split(" "));
    // 쉽게 사용하기 위해 객체로 변환
    terms = Object.fromEntries(terms);
    
    for(let i = 0; i < privacies.length; i++) {
        let [date, kind] = privacies[i];
        // 가입 날짜 정보 분리
        let [year, month, day] = date.split(".").map((val) => +val);
        month += +terms[kind];
        // 개인정보는 만료날짜 전날까지 유효
        day--;

        if (month > 12) {
            // 딱 떨어지는 경우
            if (month % 12 === 0) {
                // 만약 12월 + 12개월이면 24일 때,
                // 2년이 증가하는게 아니라, 다음해 12월이 되어야 하기에 -1을 함
                year += parseInt(month/12) - 1;
                month = 12;
            } else {
                year += parseInt(month/12);
                month = month % 12;
            }
        }
        
        // 하루 전까지 유효할 때 day가 0이 되면 전달 28일이 되어야 함
        if (day === 0) {
            month--;
            day = 28;
            if (month === 0) {
                year--;
                month = 12;
            }
        }
        
        // 유효기간이 만료되었을 때마다 continue로 다음 개인정보 확인
        if (year < curYear) {
            result.push(i+1);
            continue;
        } else if (year === curYear) {
            if (month < curMonth) {
                result.push(i+1);
                continue;
            } else if (month === curMonth) {
                if (day < curDay) {
                    result.push(i+1);
                    continue;
                }
            }
        }
    }
    return result
}