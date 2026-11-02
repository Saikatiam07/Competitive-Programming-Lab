s = "{[()]}"
stack = []
pairs = {')': '(', '}': '{', ']': '['}
for ch in s:
    if ch in "({[":
        stack.append(ch)

    elif ch in ")}]":
        if not stack or stack[-1] != pairs[ch]:
            print("Invalid Parentheses")
            break
        stack.pop()
else:
    if not stack:
        print("Valid Parentheses")
    else:
        print("Invalid Parentheses")
        
        #output:
        # Valid Parentheses
        #