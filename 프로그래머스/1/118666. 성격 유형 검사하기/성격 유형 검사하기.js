function solution(survey, choices) {
    let result = "";
    const mbti = { R: 0, T: 0, C: 0, F: 0, J: 0, M: 0, A: 0, N: 0 };
    let surveyType;
    
    for (let i = 0; i < survey.length; i++) {
        surveyType = survey[i].split("");
        
        if (choices[i] > 4) {
            mbti[surveyType[1]] += choices[i]-4;
        }
        else if (choices[i] < 4) {
            mbti[surveyType[0]] += 4-choices[i]
        }
    }
    
    if (mbti.R > mbti.T) {
        result += "R";
    } else if (mbti.R === mbti.T) {
        result += "R"
    }else {
        result += "T"
    }
    
    if (mbti.C > mbti.F) {
        result += "C";
    } else if (mbti.C === mbti.F) {
        result += "C"
    }else {
        result += "F"
    }
    
    if (mbti.J > mbti.M) {
        result += "J";
    } else if (mbti.J === mbti.M) {
        result += "J"
    }else {
        result += "M"
    }
    
    if (mbti.A > mbti.N) {
        result += "A";
    } else if (mbti.A === mbti.N) {
        result += "A"
    }else {
        result += "N"
    }
    
    return result;
}