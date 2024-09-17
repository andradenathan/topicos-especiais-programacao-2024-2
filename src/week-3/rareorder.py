from collections import defaultdict, deque

def determine_collating_sequence(strings):
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    unique_chars = set()

    for s in strings:
        unique_chars.update(s)

    def add_edge(u, v):
        if v not in graph[u]:
            graph[u].add(v)
            in_degree[v] += 1

    for i in range(len(strings) - 1):
        s1, s2 = strings[i], strings[i + 1]
        min_length = min(len(s1), len(s2))
        for j in range(min_length):
            if s1[j] != s2[j]:
                add_edge(s1[j], s2[j])
                break

    zero_in_degree = deque([c for c in unique_chars if in_degree[c] == 0])
    topological_order = []

    while zero_in_degree:
        node = zero_in_degree.popleft()
        topological_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    return ''.join(topological_order)

def main():
    strings = []
    while True:
        line = input().strip()
        if line == '#':
            break
        strings.append(line)

    
    collating_sequence = determine_collating_sequence(strings)
    print(collating_sequence)


main()
