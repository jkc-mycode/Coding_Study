def solution(array, commands):
    result = []
    for i in range(len(commands)):
        val = array[commands[i][0] - 1:commands[i][1]]
        val.sort()
        result.append(val[commands[i][2] - 1])
    return result