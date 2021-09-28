def quick_sort(x):
    if not x: return []
    if len(x) == 1:
        return x
    l, c, r = [], [], []
    x[0], x[len(x) // 2] = x[len(x) // 2], x[0]
    c.append(x[0])
    for i in range(1, len(x)):
        if x[i] < x[0]:
            l.append(x[i])
        elif x[i] == x[0]:
            c.append(x[i])
        elif x[i] > x[0]:
            r.append(x[i])
    return quick_sort(l) + c + quick_sort(r)

def search_l(x, i, l, r):
    if l < r:
        m = (r + l) // 2
        if x[m] <= i:
            return search_l(x, i, m + 1, r)
        else:
            return search_l(x, i, l, m - 1) if m != l else search_l(x, i, l, m)
    return l+1 if x[l] <= i else l

def search_r(x, i, l, r):
    if l < r:
        m = (r + l) // 2
        if x[m] < i:
            return search_r(x, i, m + 1, r)
        else:
            return search_r(x, i, l, m - 1) if m != l else search_r(x, i, l, m)
    return l-1 if x[l] >= i else l
    
def main():
    l, r = [], []
    n, m = [int(i) for i in input().split()]
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        l.append(x)
        r.append(y)
    dots = [int(i) for i in input().split()]
    l = quick_sort(l)
    r = quick_sort(r)
    for dot in dots:
        x = search_l(l, dot, 0, len(l) - 1)
        y = search_r(r, dot, 0, len(l) - 1)
        print(x - y - 1, end=' ')

if __name__ == '__main__':
    main()
