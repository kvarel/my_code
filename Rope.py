class Node:

    def __init__(self, key):
        self.key = key
        self.r = None
        self.l = None
        self.h = 1
        self.s = 1

    def __str__(self):
        return f'[key: {self.key}, l: {self.l}, r: {self.r}, h: {self.h}, s: {self.s}]'


class Rope:

    @staticmethod
    def hs_update(*nodes):
        for node in nodes:
            node.s = Rope.s(node.l) + Rope.s(node.r) + 1
            node.h = max(Rope.h(node.l), Rope.h(node.r)) + 1

    @staticmethod
    def h(node):
        return node.h if node else 0

    @staticmethod
    def s(node):
        return node.s if node else 0

    @staticmethod
    def key(node):
        return str(node.key) if node else ''

    @staticmethod
    def add(key, node):
        if node is None:
            return Node(key)
        else:
            node.r = Rope.add(key, node.r)
            Rope.hs_update(node)
            return Rope.balans(node)

    @staticmethod
    def balans_l(node):
        top = node.r
        node.r = top.l
        top.l = node
        return top

    @staticmethod
    def balans_r(node):
        top = node.l
        node.l = top.r
        top.r = node
        return top

    @staticmethod
    def big_balans_l(node):
        top = node.r.l
        node.r.l = top.r
        top.r = node.r
        node.r = top.l
        top.l = node
        return top

    @staticmethod
    def big_balans_r(node):
        top = node.l.r
        node.l.r = top.l
        top.l = node.l
        node.l = top.r
        top.r = node
        return top

    @staticmethod
    def balans(node):
        while Rope.h(node.r) - Rope.h(node.l) > 1:
            if Rope.h(node.r.r) > Rope.h(node.r.l):
                node = Rope.balans_l(node)
                Rope.hs_update(node.l, node)
                return node
            else:
                node = Rope.big_balans_l(node)
                Rope.hs_update(node.r, node.l, node)
                return node
        while Rope.h(node.l) - Rope.h(node.r) > 1:
            if Rope.h(node.l.l) > Rope.h(node.l.r):
                node = Rope.balans_r(node)
                Rope.hs_update(node.r, node)
                return node
            else:
                node = Rope.big_balans_r(node)
                Rope.hs_update(node.r, node.l, node)
                return node
        else:
            return node

    @staticmethod
    def split(number, node):
        if node == None:
            return (None, None)
        if number < Rope.s(node.l) + 1:
            (v1, v2) = Rope.split(number, node.l)
            V = Rope.Rope_merge_with_root(v2, node.r, node)
            return (v1, V)
        else:
            (v1, v2) = Rope.split(number - Rope.s(node.l) - 1, node.r)
            V = Rope.Rope_merge_with_root(node.l, v1, node)
            return (V, v2)

    @staticmethod
    def merge_with_root(v1, v2, T):
        T.l = v1
        T.r = v2
        return T

    @staticmethod
    def merge(v1, v2):
        if v1 is None:
            return v2
        if v2 is None:
            return v1
        T = Rope.max(v1)
        v1 = Rope.delete(v1)
        return Rope.Rope_merge_with_root(v1, v2, T)

    @staticmethod
    def max(node):
        if node.r:
            return Rope.max(node.r)
        else:
            return node

    @staticmethod
    def delete(node):
        if node.r:
            node.r = Rope.delete(node.r)
            Rope.hs_update(node)
            return node
        else:
            return None if node.l is None else node.l

    @staticmethod
    def Rope_merge_with_root(v1, v2, T):
        if abs(Rope.h(v1) - Rope.h(v2)) <= 1:
            Rope.merge_with_root(v1, v2, T)
            Rope.hs_update(T)
            return T
        else:
            if Rope.h(v1) > Rope.h(v2):
                t = Rope.Rope_merge_with_root(v1.r, v2, T)
                v1.r = t
                Rope.hs_update(v1.r, v1)
                return Rope.balans(v1)
            else:
                t = Rope.Rope_merge_with_root(v1, v2.l, T)
                v2.l = t
                Rope.hs_update(v2.l, v2)
                return Rope.balans(v2)

    @staticmethod
    def rope(i, j, k, node):
        if k == i:
            return node
        v1, v2 = Rope.split(i, node)
        v2, v3 = Rope.split(j-i+1, v2)
        if k == 0:
            v1 = Rope.merge(v2, v1)
            node = Rope.merge(v1, v3)
            return node
        if k < i:
            v4, v5 = Rope.split(k, v1)
            v1 = Rope.merge(v4, v2)
            v1 = Rope.merge(v1, v5)
            node = Rope.merge(v1, v3)
            return node
        elif k > i:
            v4,v5 = Rope.split(k-i, v3)
            v3 = Rope.merge(v4, v2)
            v3 = Rope.merge(v3, v5)
            node = Rope.merge(v1,v3)
            return node
        
    @staticmethod
    def rez(node):
        if node is None:
            return ''
        if node.l == node.r == None:
            return Rope.key(node)
        else:
            return Rope.rez(node.l) + Rope.key(node) + Rope.rez(node.r)

def main():
    string = input()
    node = None
    for i in string:
        node = Rope.add(i, node)
    for i in range(int(input())):
        z, x, c = map(int, input().split())
        node = Rope.rope(z, x, c, node)
    print(Rope.rez(node))

if __name__ == '__main__':
    main()
