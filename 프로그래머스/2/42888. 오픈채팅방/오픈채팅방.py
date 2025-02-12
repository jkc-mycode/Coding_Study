def solution(record):
    result = []
    record = [i.split(" ") for i in record]
    record_uid = {}
    temp = []
    
    for r in record:
        if len(r) > 2:
            record_uid[r[1]] = r[2]
        if  r[0] == "Enter":
            temp.append([r[1], r[0]])
        elif r[0] == "Leave":
            temp.append([r[1], r[0]])
        elif r[0] == "Change":
            record_uid[r[1]] = r[2]
    
    for i in temp:
        if i[1] == "Enter":
            result.append(f"{record_uid[i[0]]}님이 들어왔습니다.")
        elif i[1] == "Leave":
            result.append(f"{record_uid[i[0]]}님이 나갔습니다.")
    
    return result
    