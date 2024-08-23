test_cases = int(input())

for _ in range(test_cases):
    number = input()
    number_size = len(number)
    min_steps = float('inf')

    for i in range(number_size):
        for j in range(i + 1, number_size):
            if (number[i] == '0' and number[j] == '0') or \
            (number[i] == '2' and number[j] == '5') or \
            (number[i] == '5' and number[j] == '0') or \
            (number[i] == '7' and number[j] == '5'):
                steps = (number_size - j - 1) + (j - i - 1)
                min_steps = min(min_steps, steps)

    print(min_steps)