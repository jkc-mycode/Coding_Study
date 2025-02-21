from collections import deque

def bfs(start_node, wires_dict, visited):
    queue = deque([start_node])
    count = 0
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            count += 1
            for neighbor in wires_dict[node]:
                queue.append(neighbor)
                
    return count

def solution(n, wires):
    min_diff = n
    
    for k in range(len(wires)):
        remaining_wires = wires[:k] + wires[k+1:]
        
        wires_dict = {i: [] for i in range(1, n+1)}
        for wire in remaining_wires:
            wires_dict[wire[0]].append(wire[1])
            wires_dict[wire[1]].append(wire[0])
        
        visited = set()
        size1 = bfs(wires[k][0], wires_dict, visited)
        size2 = n - size1
        
        min_diff = min(min_diff, abs(size1 - size2))
    
    return min_diff