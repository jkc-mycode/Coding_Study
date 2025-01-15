def solution(id_list, report, k):
    report = [r.split(" ") for r in report]
    
    report_list = {i: set() for i in id_list}
    report_count = {i: 0 for i in id_list}
    
    for i in report:
        report_list[i[0]].add(i[1])
    
    for i in report_list:
        for j in report_list[i]:
            report_count[j] += 1
    
    stopped_list = [user for user in report_list if report_count[user] >= k]
    
    result = []
    
    for i in report_list:
        count = 0
        for j in report_list[i]:
            if j in stopped_list:
                count += 1
        result.append(count)
    
    return result