def count_interesting_numbers(n):
    count = n // 10  
    if n % 10 == 9:  
        count += 1
    return count


t = int(input())  
for _ in range(t):
    n = int(input())
    print(count_interesting_numbers(n))
