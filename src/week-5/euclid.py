def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, gcd = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return x, y, gcd

while True:
    try:
        data = input().split()
        a, b = map(int, data)
        x, y, gcd = extended_gcd(a, b)
        print(x, y, gcd)
    except EOFError:
        break