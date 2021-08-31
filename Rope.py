class Node:

    def __init__(self, key):
        self.key = key
        self.r = None
        self.l = None
        self.h = 1

    def __str__(self):
        return f'[[[key {self.key} | l {self.l} | r {self.r} | h {self.h}]]]'

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
                Rope.h_update(node.l)
                Rope.h_update(node)
                return node
            else:
                node = Rope.big_balans_l(node)
                Rope.h_update(node.r)
                Rope.h_update(node.l)
                Rope.h_update(node)
                return node
        while Rope.h(node.l) - Rope.h(node.r) > 1:
            if Rope.h(node.l.l) > Rope.h(node.l.r):
                node = Rope.balans_r(node)
                Rope.h_update(node.r)
                Rope.h_update(node)
                return node
            else:
                node = Rope.big_balans_r(node)
                Rope.h_update(node.r)
                Rope.h_update(node.l)
                Rope.h_update(node)
                return node
        else:
            return node
        
    @staticmethod
    def split(number, node):
        if node == None:
            return None
        if number == node.h+1:
            v1 = node.l
            node.l = None
            return (v1, node)
        if number > node.l.h:
            v2 = node.r
            node.r = None
            return(node, Rope.split(number-Rope.h(node.l)-1, v2))
        if number < node.l.h:
            pass
            
            
            
    @staticmethod
    def merge(v1, v2):
        pass
        
        

node = Node(7)
node = Rope.add(10, node)
node = Rope.add(15, node)
node = Rope.add(20, node)
node = Rope.add(25, node)
print(node)
