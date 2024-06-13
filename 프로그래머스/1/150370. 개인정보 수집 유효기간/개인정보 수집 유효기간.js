function solution(today, terms, privacies) {
    const result = [];
    let [curYear, curMonth, curDay] = today.split(".").map((val) => +val);
    privacies = privacies.map((val) => val.split(" "));
    terms = terms.map((val) => val.split(" "));
    terms = Object.fromEntries(terms);
    
    console.log(privacies)
    
    for(let i = 0; i < privacies.length; i++) {
        let [date, kind] = privacies[i];
        let [year, month, day] = date.split(".").map((val) => +val);
        month += +terms[kind];
        day--;
        
        

        if (month > 12) {
            if (month % 12 === 0) {
                year += parseInt(month/12) - 1;
                month = 12;
            } else {
                year += parseInt(month/12);
                month = month % 12;
            }
        }
        
        if (day === 0) {
            month--;
            day = 28;
            if (month === 0) {
                year--;
                month = 12;
            }
        }
        
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