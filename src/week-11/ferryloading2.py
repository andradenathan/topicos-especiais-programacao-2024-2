test_cases = int(input())

for _ in range(test_cases):
    capacity, crossing_time, num_cars = map(int, input().split())
    arrival_times = [int(input()) for _ in range(num_cars)]
    
    arrival_times.sort()
    
    trips = 0
    current_time = 0
    pos = 0
    
    if num_cars % capacity == 0:
        current_time = arrival_times[capacity - 1] + 2 * crossing_time
        pos = capacity
    else:
        current_time = arrival_times[num_cars % capacity - 1] + 2 * crossing_time
        pos = num_cars % capacity
    
    while pos < num_cars:
        if current_time >= arrival_times[pos + capacity - 1]:
            current_time += 2 * crossing_time
        else:
            current_time = arrival_times[pos + capacity - 1] + 2 * crossing_time
        pos += capacity
    
    current_time -= crossing_time
    
    print(f"{current_time} {(num_cars + capacity - 1) // capacity}")