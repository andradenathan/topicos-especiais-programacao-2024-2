mirrored_string = {
    "A": "A",
    "E": "3",
    "H": "H",
    "I": "I",
    "J": "L",
    "L": "J",
    "M": "M",
    "O": "O",
    "S": "2",
    "T": "T",
    "U": "U",
    "V": "V",
    "W": "W",
    "X": "X",
    "Y": "Y",
    "Z": "5",
    "1": "1",
    "2": "S",
    "3": "E",
    "5": "Z",
    "8": "8"
}

def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False 

def is_mirrored_string(s):
    mirrored = ""
    for c in s:
        if c in mirrored_string:
            mirrored += mirrored_string[c]
        else:
            return False
    if mirrored == s[::-1]:
        return True
    return False

if __name__ == "__main__":
    while True:
        try:
            s = input()
            if is_palindrome(s) and is_mirrored_string(s):
                print(f"{s} -- is a mirrored palindrome.")
            elif is_palindrome(s):
                print(f"{s} -- is a regular palindrome.")
            elif is_mirrored_string(s):
                print(f"{s} -- is a mirrored string.")
            else:
                print(f"{s} -- is not a palindrome.")
            print()
        except EOFError:
            break