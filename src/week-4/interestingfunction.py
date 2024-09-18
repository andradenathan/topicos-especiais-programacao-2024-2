def count_digit_changes(l, r):
    changes = 0
    while l > 0 or r > 0:
        changes += r - l
        l //= 10
        r //= 10
    return changes

def main():
    t = int(input())  
    for _ in range(t):
        l, r = map(int, input().split())  
        print(count_digit_changes(l, r))

if __name__ == "__main__":
    main()