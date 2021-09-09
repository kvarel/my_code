def main(string):
    stack = ['x', 'x']
    string = string.split()
    for i in string:
        if i.isdigit():
            if str(stack[-2]).isdigit() and stack[-1] in '*/':
                y = stack.pop()
                x = stack.pop()
                stack.append(x*int(i) if y=='*' else x/int(i))
            else: stack.append(int(i))
        if i in '+-*/':
            stack.append(i)
    while len(stack) > 3:
        x = stack.pop()
        y = stack.pop()
        z = stack.pop()
        stack.append(z+x if y == '+' else z-x)
    return(stack[2])
    
def test():
    from random import randint as r, choice as c
    for i in range(100):
        x = r(1, 100)
        y = r(1, 100)
        b = c('-')
        z = c(['*', '/'])
        print(x, b, x, z, y)
        assert main(f'{str(x)} {b} {str(x)} {z} {str(y)}') == x-x*y if z == '*' else x-x/y
        

if __name__ == '__main__':
    print(main('4 / 2 + 18 - 2 * 6'))
