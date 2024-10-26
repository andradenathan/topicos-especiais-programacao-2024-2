def check_winner(grid, player):
    for i in range(3):
        if all(grid[i][j] == player for j in range(3)):  
            return True
        if all(grid[j][i] == player for j in range(3)):  
            return True
    if all(grid[i][i] == player for i in range(3)):      
        return True
    if all(grid[i][2 - i] == player for i in range(3)):  
        return True
    return False

def is_valid_tic_tac_toe(grid):
    x_count = sum(row.count('X') for row in grid)
    o_count = sum(row.count('O') for row in grid)

    if not (x_count == o_count or x_count == o_count + 1):
        return False

    x_wins = check_winner(grid, 'X')
    o_wins = check_winner(grid, 'O')
    
    if x_wins and o_wins:
        return False

    if x_wins and x_count != o_count + 1:
        return False
    
    if o_wins and x_count != o_count:
        return False

    return True

n = int(input())
grids = []

for _ in range(n):
    grid = [input().strip() for _ in range(3)]
    input()
    grids.append(grid)

for grid in grids:
    if is_valid_tic_tac_toe(grid):
        print('yes')
    else:
        print('no')
