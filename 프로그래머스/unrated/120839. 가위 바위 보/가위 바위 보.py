def solution(rsp):
    return ''.join(["0" if i=="2" else "2" if i=="5" else "5" for i in rsp])