"""
Write a function that takes in a Binary tree (where nodes have an addtional pointer to their parrent node).
find the node's successor which is the next node to be visited when traversing the tree using in-order traversal.
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(n) time & O(n) space
def findSuccessor(tree, node):
    arr = []
    arr = inOrderTraverse(tree, arr)
    for i in range(len(arr)):
        if arr[i].value == node:
            return arr[i+1].value


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree)
        inOrderTraverse(tree.right, array)
    return array


tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.left.right = BinaryTree(5)
tree.left.left = BinaryTree(4)
tree.left.left.left = BinaryTree(6)
tree.right = BinaryTree(3)

print(findSuccessor(tree, tree.left.left.value))
