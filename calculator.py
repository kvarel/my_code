def main(string):
    global i
    stack = ['x', 'x']
    while i < len(string):
        if string[i].isdigit():
            if str(stack[-2]).isdigit() and stack[-1] in '*/':
                y = stack.pop()
                x = stack.pop()
                stack.append(x*int(string[i]) if y=='*' else x/int(string[i]))
            else: stack.append(int(string[i]))
            i += 1
        elif string[i] in '+-*/':
            stack.append(string[i])
            i += 1
        elif string[i] == '(':
            i += 1
            z = main(string)
            if str(stack[-2]).isdigit() and stack[-1] in '*/':
                y = stack.pop()
                x = stack.pop()
                stack.append(x*z if y=='*' else x/z)
            else: stack.append(z)
        elif string[i] == ')':
            i += 1
            break
    while len(stack) > 3:
        x = int(stack.pop(2))
        y = stack.pop(2)
        z = int(stack.pop(2))
        stack.insert(2, z+x if y == '+' else x-z)
    return(stack[2])


if __name__ == '__main__':
    i = 0
    string = input().split()
    print(main(string))
