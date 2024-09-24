def solution(participant, completion):
    dict_participant = {}
    for val in participant:
        if val in dict_participant:
            dict_participant[val] += 1
        else:
            dict_participant[val] = 1
    
    for val in completion:
        if val in dict_participant:
            dict_participant[val] -= 1
    
    for key, val in dict_participant.items():
        if val != 0:
            return key
    
    