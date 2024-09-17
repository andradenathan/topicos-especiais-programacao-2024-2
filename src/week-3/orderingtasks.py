from collections import deque, defaultdict

def topological_sort(n, dependencies):
    adj_list = defaultdict(list)
    in_degree = [0] * (n + 1)

    for i, j in dependencies:
        adj_list[i].append(j)
        in_degree[j] += 1

    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    topological_order = []

    while queue:
        current_task = queue.popleft()
        topological_order.append(current_task)

        for neighbor in adj_list[current_task]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return topological_order

def process_tasks():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        dependencies = []
        for _ in range(m):
            i, j = map(int, input().split())
            dependencies.append((i, j))

        result = topological_sort(n, m, dependencies)
        
        print(" ".join(map(str, result)))
process_tasks()
