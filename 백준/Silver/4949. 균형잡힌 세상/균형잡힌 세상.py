while True:
    a = input()
    if a == '.':
        break    
    s = []

    for i in a:
        if i == '[':
            s.append(i)
        elif i == ']':
            if s and s[-1] == '[':
                s.pop()
            else:
                s.append(i)
        elif i == '(':
            s.append(i)
        elif i == ')':
            if s and s[-1] == '(':
                s.pop()
            else:
                s.append(i)
        elif i == '.':
            break
    if s:
        print('no')
    else:
        print('yes')