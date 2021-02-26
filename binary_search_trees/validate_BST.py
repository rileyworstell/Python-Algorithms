"""
Function that takes in a BST and returns a bool representing valid or not.
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) Time & O(d) Space
def validateBst(tree, minValue=float('-inf'), maxValue=float('inf')):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBst(tree.left, minValue, tree.value)
    rightIsValid = validateBst(tree.right, tree.value, maxValue)
    return leftIsValid and rightIsValid


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

print(validateBst(tree))
