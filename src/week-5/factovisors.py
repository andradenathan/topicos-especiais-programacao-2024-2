def prime_factors(m):
    factors = {}
    d = 2
    while d * d <= m:
        while (m % d) == 0:
            if d in factors:
                factors[d] += 1
            else:
                factors[d] = 1
            m //= d
        d += 1
    if m > 1:
        factors[m] = 1
    return factors

def count_prime_in_factorial(n, p):
    count = 0
    power_of_p = p
    while power_of_p <= n:
        count += n // power_of_p
        if power_of_p > n // p:
            break 
        power_of_p *= p
    return count

def divides_factorial(n, m):
    if m == 0:
        return False 
    if m == 1:
        return True 
    
    factors_m = prime_factors(m)
    

    for prime, count_in_m in factors_m.items():
        count_in_n_fact = count_prime_in_factorial(n, prime)
        if count_in_n_fact < count_in_m:
            return False
    return True

def process_input():
    try:
        while True:
            line = input().strip()
            if not line:
                break
            n, m = map(int, line.split())
            if divides_factorial(n, m):
                print(f"{m} divides {n}!")
            else:
                print(f"{m} does not divide {n}!")
    except EOFError:
        pass

process_input()
