while True:
    m, n = map(int, input().split())

    if (m, n) == (0, 0):
        break

    if m == 1 or n == 1:
        total_knights = max(m, n)
    elif m == 2 or n == 2:
        total_knights = (max(m, n) // 4) * 4 + min(2, max(m, n) % 4) * 2
    else:
        total_knights = (m * n + 1) // 2

    print(f"{total_knights} knights may be placed on a {m} row {n} column board.")