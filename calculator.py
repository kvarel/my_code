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
        elif string[i] in '+-*/':
            stack.append(string[i])
        elif string[i] == '(':
            i += 1
            z = main(string)
            if str(stack[-2]).isdigit() and stack[-1] in '*/':
                y = stack.pop()
                x = stack.pop()
                stack.append(x*z if y=='*' else x/z)
            else: stack.append(int(string[i]))
        elif string[i] == ')':
            i += 1
            break
        i += 1
    while len(stack) > 3:
        x = int(stack.pop())
        y = stack.pop()
        z = int(stack.pop())
        stack.append(z+x if y == '+' else z-x)
    return(stack[2])


if __name__ == '__main__':
    i = 0
    string = input().split()
    print(main(string))
