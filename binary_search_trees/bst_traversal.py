"""
Write three functions that take in a BST and an empty array, traverse the BST, add its nodes to the input array and return that array.
The functions should be traversing in-order, pre-order, and post-order
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


# Create Tree
tree = BST(10)
tree.left = BST(5)
tree.left.left = BST(2)
tree.left.left.left = BST(1)
tree.left.right = BST(5)
tree.right = BST(15)
tree.right.right = BST(22)
"""
Tree
            10
        5        15
      2   5         22
    1            
"""
arr = []
print(inOrderTraverse(tree, arr))
arr = []
print(preOrderTraverse(tree, arr))
arr = []
print(postOrderTraverse(tree, arr))
