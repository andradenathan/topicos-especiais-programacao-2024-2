import sys
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def find_two_primes(n):
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            return i, n - i
    return None

for line in sys.stdin:
    n = int(line.strip())
    
    if n < 8:
        print("Impossible.")
        continue
    
    if n % 2 == 0:
        p1, p2 = 2, 2
        remainder = n - 4
    else:
        p1, p2 = 2, 3
        remainder = n - 5
    
    result = find_two_primes(remainder)
    if result:
        p3, p4 = result
        print(p1, p2, p3, p4)
    else:
        print("Impossible.")
