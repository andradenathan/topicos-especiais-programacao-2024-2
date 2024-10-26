import math
import sys

def largest_prime_divisor(n):
    if n == 0 or abs(n) == 1:
        return -1
    
    n = abs(n)
    largest_prime = -1
    distinct_prime_count = 0
    
    if n % 2 == 0:
        distinct_prime_count += 1
        largest_prime = 2
        while n % 2 == 0:
            n //= 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            distinct_prime_count += 1
            largest_prime = i
            while n % i == 0:
                n //= i
    
    if n > 2:
        distinct_prime_count += 1
        largest_prime = n
    
    if distinct_prime_count > 1:
        return largest_prime
    else:
        return -1
    
input = sys.stdin.read
data = input().splitlines()

for line in data:
    n = int(line)
    if n == 0:
        break
    print(largest_prime_divisor(n))
