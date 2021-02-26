"""
Create BST class that supports insert, remove, and contain.
"""


# O(log(n)) Time & O(1) Space for each operation
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value, direction=None):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value, set_return=False):
        if self.value == value:
            set_return = True
        if self.value <= value and self.right is not None:
            set_return = self.right.contains(value, set_return)
        elif self.value > value and self.left is not None:
            set_return = self.left.contains(value, set_return)
        return set_return

    def remove(self, value):
        pass
        # T0D0


# Create Tree
tree = BST(10)
tree.left = BST(5)
tree.left.left = BST(2)
tree.left.left.left = BST(1)
tree.left.right = BST(5)
tree.right = BST(15)
tree.right.left = BST(13)
tree.right.left.right = BST(14)
tree.right.right = BST(22)
"""
Tree
            10
        5        15
      2   5    13   22
    1            14
"""
target = 12

# print(tree.contains(1))
# print(tree.contains(100000))
# print(tree.insert(12))
# print(tree.right.left.left.value)

print(tree.remove(1))
print(tree.left.left.left.value)
