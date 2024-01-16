def solution(babbling):
    count = 0
    for i in babbling:
        temp = i
        for j in ["aya", "ye", "woo", "ma"]:
            temp = temp.replace(j, "_")
        if temp.replace("_", "") == "":
            count += 1
    return count