test_cases = int(input())

results = []

for _ in range(test_cases):
    types_of_candies = int(input())
    candies_of_type = list(map(int, input().split(" ")))

    if types_of_candies == 1:
        if candies_of_type[0] == 1:
            results.append("YES")
        else:
            results.append("NO")
    else:
        candies_of_type.sort(reverse=True)
        if candies_of_type[0] - candies_of_type[1] > 1:
            results.append("NO")
        else:
            results.append("YES")

print("\n".join(results))