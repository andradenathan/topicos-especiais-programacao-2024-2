import sys

def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def find_maximum_n(s):
    lps = compute_lps(s)
    len_s = len(s)
    smallest_repeating_unit_length = len_s - lps[-1]
    
    if len_s % smallest_repeating_unit_length == 0:
        return len_s // smallest_repeating_unit_length
    else:
        return 1

def main():
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    for line in data:
        if line == '.':
            break
        s = line
        print(find_maximum_n(s))

main()
