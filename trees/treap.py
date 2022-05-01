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

    """
    Insert if value does not exist in treap
    """
    def insert(self, value, priority):
        if value not in self.priorities.keys():
            self.priorities[value] = priority
            self.root = self.__ins(self.root, value, priority)
        return self.root

    def __del (self, root, value):
        if root == None:
            pass
        elif root.value > value:
            root.left = self.__del(root.left, value)
        elif root.value < value:
            root.right = self.__del(root.right, value)
        # If we find the root
        elif root.value == value:
            if root.left == root.right == None:
                root = None
            elif root.left == None:
                root = root.right
            elif root.right == None:
                root = root.left
            elif self.priorities[root.left.value] < self.priorities[root.right.value]:
                root = self.left_rotate(root)
                root.right = self.__del(root.right, value)
            else:
                root = self.right_rotate(root)
                root.left = self.__del(root.left, value)
        return root
        
    def delete(self, value):
        if value in self.priorities.keys():
            self.root = self.__del(self.root, value)
        return self.root

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
print("Initialize `simulate`")
print(treap)
print("insert y(0)")
treap.insert('y', 0)
print(treap)
print("delete s")
treap.delete('s')
print(treap)