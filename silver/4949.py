while True:
    inp = input()
    stack = []

    if inp == '.':
        break

    for i in inp:
        if i == '(' or i == '[':
            stack.append(i)
            
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
        
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break

    if stack:
        print('no')
    else:
        print('yes')