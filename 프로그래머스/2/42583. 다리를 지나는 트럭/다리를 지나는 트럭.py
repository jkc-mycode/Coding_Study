from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    result = 0
    cur_weight = 0
    
    for truck in truck_weights:
        while True:
            if cur_weight + truck - bridge[0] <= weight:
                cur_weight += truck
                cur_weight -= bridge.popleft()
                bridge.append(truck)
                result += 1
                break
            else:
                cur_weight -= bridge.popleft()
                bridge.append(0)
                result += 1
    
    return result + bridge_length