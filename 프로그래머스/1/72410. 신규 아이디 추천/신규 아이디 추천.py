def solution(new_id):
    result = ""
    temp = ""
    prev_word = ""
    
    # 1단계
    new_id = new_id.lower()

    for word in new_id:
        # 2단계
        if word.isalnum() or word in ["-", "_", "."]:
            temp += word

    for word in temp:
        # 3단계
        if word == "." and prev_word == ".":
            continue
        result += word
        prev_word = word

    # 4단계
    if result[0] == ".":
        result = result[1:]
    if len(result) > 0 and result[-1] == ".":
        result = result[:-1]

    # 5단계
    if len(result) == 0:
        result += "a"

    # 6단계
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == ".":
            result = result[:-1]

    # 7단계
    while len(result) < 3:
        result += result[-1]

    return result