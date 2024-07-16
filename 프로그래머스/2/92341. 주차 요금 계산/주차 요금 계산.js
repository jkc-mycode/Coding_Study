function solution(fees, records) {
    const parking = {};
    
    records.forEach((val) => {
        const [time, num, status] = val.split(" ");
        const [hour, min] = time.split(":");
        // 시간을 분으로 통일
        const totalMinute = hour * 60 + +min;
        
        // 처음 입고 시 시간은 0분부터 시작
        if(!parking[num]) {
            parking[num] = { time: 0, num }
        }
        
        // 현재 차번호의 상태 기록
        // 계속 IN일수도 있고 OUT으로 바뀔 수도 있음
        parking[num].status = status;
        
        // 입차된 시간 기록
        if (status === 'IN') {
            parking[num].inTime = totalMinute;
        } else {
            // 출차일 때는 출차 시간(분) - 입차 시간(분)
            parking[num].time += totalMinute - parking[num].inTime;
        }
    })
    
    return Object.values(parking)
        .sort((a, b) => a.num - b.num)
        .map((val) => {
            // 최종적으로 나가지 않았을 때
            if (val.status === 'IN') {
                val.time += 1439 - val.inTime;
            }
            // 기본 시간을 넘지 않으면
            if (fees[0] > val.time) {
                return fees[1];
            }
        
            return fees[1] + Math.ceil((val.time - fees[0]) / fees[2]) * fees[3];
        })
}