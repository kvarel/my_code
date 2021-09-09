def insert(x):
    if not k:
        k.append(x)
    else:
        k.append(x)
        up(len(k)-1)
def up(x):
    if x > 0:
        if k[x] > k[(x-1)//2]:
            k[x], k[(x-1)//2] = k[(x-1)//2], k[x]
            up((x-1)//2)
def extract_max():
    k[0], k[-1] = k[-1], k[0]
    print(k.pop())
    down(0)
def down(x):
    m, pos = k[x], x
    if x*2+1 < len(k) and k[x*2+1] > m: m, pos = k[x*2+1], x*2+1
    if x*2+2 < len(k) and k[x*2+2] > m: m, pos = k[x*2+2], x*2+2
    if pos != x:
        k[x], k[pos] = k[pos], k[x]
        down(pos)
def main():
    n = int(input())
    for i in range(n):
        zapros = input().split()
        if len(zapros) == 2:
            insert(int(zapros[1]))
        elif len(zapros) == 1:
            extract_max()
if __name__ == '__main__':
    k = []
    main()
            
