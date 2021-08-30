class Node:

    def __init__(self, key):
        self.key = key
        self.r = None
        self.l = None
        self.h = 1

    def __str__(self):
        return f'[key {self.key} | r {self.r} | l {self.l} | h {self.h}]'

class Rope:

    @staticmethod
    def find(number, node):
        if node is None:
            return None
        if node.h == 1 and number == 1:
            return node
        if node.l:
            if number - node.l.h == 1:
                return node
            if number - node.l.h > 1:
                return Rope.find(number - node.l.h - 1, node.r)
            if number - node.l.h < 1:
                return Rope.find(number, node.l)
        else:
            return node if number < node.h else Rope.find(number - 1, node.r)

    @staticmethod
    def h_update(node):
        node.h = max([Rope.h(node.l), Rope.h(node.r)]) + 1

    @staticmethod
    def h(node):
        return node.h if node else 0

    @staticmethod
    def add(key, node):
        if node is None:
            return Node(key)
        else:
            node.r = Rope.add(key, node.r)
            Rope.h_update(node)
            return node

    @staticmethod
    def balans_l(node):
        top = node.r
        node.r = top.l
        top.l = node

    @staticmethod
    def balans_r(node):
        top = node.l
        node.l = top.r
        top.r = node
        node = top

    @staticmethod
    def big_balans_l(node):
        top = node.r.l
        node.r.l = top.r
        top.r = node.r
        node.r = top.l
        top.l = node

    @staticmethod
    def big_balans_r(node):
        top = node.l.r
        node.l.r = top.l
        top.l = node.l
        node.l = top.r
        top.r = node

node = Node(7)
