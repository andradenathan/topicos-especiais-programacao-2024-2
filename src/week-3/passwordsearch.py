from collections import defaultdict

def find_most_frequent_password(N, text):
    cont = defaultdict(int)
    L = len(text)
    
    for i in range(L - N + 1):
        aux = 0
        for j in range(N):
            aux = aux * 26 + (ord(text[i + j]) - ord('a'))
        cont[aux] += 1

    best = -1
    ans_hash = None
    
    for hash_value, count in cont.items():
        if count > best:
            ans_hash = hash_value
            best = count
    
    ans = []
    for _ in range(N):
        ans.append(chr(ans_hash % 26 + ord('a')))
        ans_hash //= 26

    return ''.join(reversed(ans))

def main():
    while True:
        try:
            line = input().strip()
            if line:
                parts = line.split()
                N = int(parts[0])
                text = parts[1]
                password = find_most_frequent_password(N, text)
                print(password)
        except EOFError:
            break

if __name__ == "__main__":
    main()
