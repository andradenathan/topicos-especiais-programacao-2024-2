from itertools import permutations

n = int(input())

for _ in range(n):
    string = input()
    
    for permutacao in sorted(set(''.join(p) for p in permutations(string))):
        print(permutacao)
    print()
