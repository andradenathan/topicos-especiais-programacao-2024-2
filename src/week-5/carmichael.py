import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def fermat_test(n):
    for a in range(2, n):
        if math.gcd(a, n) == 1: 
            if pow(a, n, n) != a:
                return False
    return True

carmichael_numbers = []
for n in range(3, 65000):
    if not is_prime(n) and fermat_test(n):
        carmichael_numbers.append(n)

while True:
    n = int(input())
    if n == 0:
        break
    if n in carmichael_numbers:
        print(f"The number {n} is a Carmichael number.")
    elif is_prime(n):
        print(f"{n} is normal.")
    else:
        print(f"{n} is normal.")
