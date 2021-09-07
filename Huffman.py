class Node():
    def __init__(self, i, h):
        self.i = i
        self.l = None
        self.r = None
        self.h = h

class H():
    def __init__(self):
        self.H = list()
        self.C = dict()

    def insert(self, x):
        self.H.append(x)

    def extract(self):
        min_h, position = float('inf'), 0
        for i in range(len(self.H)):
            if self.H[i].h < min_h:
                min_h, position = self.H[i].h, i
        return self.H.pop(position)

    @staticmethod
    def huffman(s, lst):
        for i in lst:
            H.insert(s, Node(i[0], i[1]))
        while len(s.H) > 1:
            x = Node(None, 0)
            x.r = H.extract(s)
            x.l = H.extract(s)
            x.h = (x.r.h + x.l.h)
            s.insert(x)

    def code(self, x, c=''):
        if x.l is None and x.r is None:
            self.C[x.i] = c if c else '0'
        else:
            self.code(x.l, c+'1')
            self.code(x.r, c+'0')

def main():
    s = input()
    k = dict()
    for i in s:
        k[i] = 1 if i not in k else k[i] + 1
    node = H()
    H.huffman(node, k.items())
    node.code(node.H[0])
    m = ''
    for i in s:
        m += node.C[i]
    print(len(k), len(m))
    for i in sorted(node.C.items(), key= lambda x: x[1]):
        print(f'{i[0]}: {i[1]}')
    print(m)

if __name__ == '__main__':
    main()
