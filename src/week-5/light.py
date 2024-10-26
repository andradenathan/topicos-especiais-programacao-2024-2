import math

def is_last_bulb_on(n):
    if n == 0:
        return
    
    sqrt_n = int(math.sqrt(n))
    if sqrt_n * sqrt_n == n:
        return "yes"
    else:
        return "no"

while True:
    n = int(input())
    if n == 0:
        break
    print(is_last_bulb_on(n))
