test_cases = int(input())

for _ in range(test_cases):
    vertices = int(input())
    vertices_list = list(map(int, input().split()))

    height = 0
    current_level_count = 1  
    next_level_count = 0
    index = 1  

    while index < vertices:
        while current_level_count > 0:
            current_level_count -= 1
            if index < vertices:
                next_level_count += 1
                index += 1
                while index < vertices and vertices_list[index] > vertices_list[index - 1]:
                    next_level_count += 1
                    index += 1
        
        height += 1
        current_level_count, next_level_count = next_level_count, 0

    print(height)
