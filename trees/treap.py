from binarytree import Node
from requests import delete

# https://en.wikipedia.org/wiki/Treap

class Treap:
    def __init__(self, values, priorities):
        self.priorities = {}
        self.root = None
        for value, prior in zip(values, priorities):
            self.insert(value, prior)

    def __ins(self, root, value, priority):
        if root == None:
            root = Node(value)
        elif root.value > value:
            root.left = self.__ins(root.left, value, priority)
            if root.left != None and self.priorities[root.value] < self.priorities[root.left.value]:
                root = self.left_rotate(root)
        elif root.value < value:
            root.right = self.__ins(root.right, value, priority)
            if root.right != None and self.priorities[root.value] < self.priorities[root.right.value]:
                root = self.right_rotate(root)
        return root

    def insert(self, value, priority):
        self.priorities[value] = priority
        self.root = self.__ins(self.root, value, priority)

    # Delete operation needs to be done
    def __del (self, root, value):
        pass
    def delete(self, value):
        pass

    def left_rotate(self, u):
        v = u.left
        u.left = v.right
        v.right = u
        return v

    def right_rotate(self, u):
        v = u.right
        u.right = v.left
        v.left = u
        return v 

    def __str__(self):
        return self.root.__str__()

treap = Treap("eimulats", [1,7,6,5,4,3,2,8])
treap.insert('y', 0)
print(treap)