from itertools import permutations

entry = int(input())

for _ in range(entry):
    number_in_list = list(input().strip())
    for perm in permutations(number_in_list):
        number = int("".join(perm))
        if number % 60 == 0:
            print("red")
            break
    else:
        print("cyan")