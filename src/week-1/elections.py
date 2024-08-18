test_cases = int(input())

for _ in range(test_cases):
    a, b, c = list(map(int, input().split()))

    votes_amount_first_candidate = max(0, max(b, c) + 1 - a)
    votes_amount_second_candidate = max(0, max(a, c) + 1 - b)
    votes_amount_third_candidate = max(0, max(a, b) + 1 - c)

    print(f"{votes_amount_first_candidate} {votes_amount_second_candidate} {votes_amount_third_candidate}")