test_cases = int(input())

for _ in range(test_cases):
    n, k = list(map(int, input().split()))
    mice_positions = list(map(int, input().split()))
    
    mice_positions.sort(reverse=True)

    cat_position = 0
    saved_mice = 0

    for mouse_position in mice_positions:
        if mouse_position > cat_position:
            saved_mice += 1
            cat_position += (n - mouse_position)
        else:
            break
    
    print(saved_mice)