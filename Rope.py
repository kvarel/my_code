class Node:
    
    def __init__(self, key):
        self.key = key
        self.r = None
        self.l = None
        self.h = 1
        
    def __repr__(self):
        return f'key {self.key}, r {self.r}, l {self.l}, sum {self.sum}'
    
class Rope:
    
    def find(self, number, node):
        if node is None:
            return None
        if node.h == 1 and number == 1:
            return node
        if node.l:
            if number - node.l.h == 1:
                return node
            if number - node.l.h > 1:
                return Rope.find(number-node.l.h-1, node.r)
            if number - node.l.h < 1:
                return Rope.find(number, node.l)
        else:
            return node if number < node.h else Rope.find(number-1, node.r)
        
    def h_update(self, node):
        node.h = max((node.l.h, node.r.h)) + 1
        
    def add(self, key, node):
        if node is None:
            return Node(key)
        if node.r:
            node.r = Rope.add(key, node.r)
            return h_update(node)
        
