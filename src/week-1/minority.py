test_cases = int(input())

results = []

for _ in range(test_cases):
    string = input()
    count_zero = string.count('0')
    count_one = string.count('1')        

    if count_zero == count_one:
        results.append(count_zero - 1)

    elif count_zero > count_one:
        results.append(count_one)

    else:
        results.append(count_zero)

print("\n".join(map(str, results)))