import collections

def flood_fill(grid, visited, start_x, start_y, land_char, M, N):
    queue = collections.deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    size = 0

    while queue:
        x, y = queue.popleft()
        size += 1
        
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, (y + dy) % N  
            if 0 <= nx < M and not visited[nx][ny] and grid[nx][ny] == land_char:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return size

def solve():
    results = []

    while True:
        try:
            M, N = map(int, input().strip().split())
        except EOFError:
            break
        
        grid = []
        for _ in range(M):
            grid.append(list(input().strip()))
        
        X, Y = map(int, input().strip().split())
        
        input()

        land_char = grid[X][Y]

        visited = [[False] * N for _ in range(M)]

        mijid_continent_size = flood_fill(grid, visited, X, Y, land_char, M, N)

        max_continent_size = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == land_char and not visited[i][j]:
                    continent_size = flood_fill(grid, visited, i, j, land_char, M, N)
                    max_continent_size = max(max_continent_size, continent_size)
        
        results.append(str(max_continent_size))
    
    print("\n".join(results))

solve()