from collections import deque, defaultdict

def is_bipartite_and_count(graph, v, start, color):
    queue = deque([start])
    color[start] = 0 
    count = [0, 0]   
    count[0] += 1
    
    while queue:
        node = queue.popleft()
        current_color = color[node]
        
        for neighbor in graph[node]:
            if color[neighbor] == -1: 
                color[neighbor] = 1 - current_color
                count[color[neighbor]] += 1
                queue.append(neighbor)
            elif color[neighbor] == current_color: 
                return -1
        
    return min(count) if sum(count) > 1 else 1

def minimum_guards(v, e, edges):
    graph = defaultdict(list)
    for f, t in edges:
        graph[f].append(t)
        graph[t].append(f)
    
    color = [-1] * v
    total_guards = 0
    
    for i in range(v):
        if color[i] == -1: 
            guards_needed = is_bipartite_and_count(graph, v, i, color)
            if guards_needed == -1:
                return -1
            total_guards += guards_needed
    
    return total_guards

def main():
    T = int(input().strip())
    results = []
    for _ in range(T):
        v, e = map(int, input().strip().split())
        edges = [tuple(map(int, input().strip().split())) for _ in range(e)]
        results.append(minimum_guards(v, e, edges))
    
    for result in results:
        print(result)

main()