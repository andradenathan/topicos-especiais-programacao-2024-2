tests_case = int(input())

for _ in range(tests_case):
    string = input()

    stack = []
    for char in string:
        if char in ['(', '[']:
            stack.append(char)
        elif char == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif char == ']' and stack and stack[-1] == '[':
            stack.pop()
        else:
            stack.append(char)
        
    print("Yes" if not stack else "No")