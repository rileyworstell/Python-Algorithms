"""
function that takes in a BST and a target and returns the closest value to that target contained in the tree.
"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(log(n)) Time & O(1) Space
def findClosestValueInBST(tree, target):
    closest = tree.value
    return helper(tree, target, closest)


def helper(current, target, closest):
    while current is not None:
        if abs(current.value - target) < abs(closest - target):
            closest = current.value
            if closest == target:
                return closest
        if target < current.value:
            current = current.left
        elif target >= current.value:
            current = current.right
    return closest


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

print(findClosestValueInBST(tree, target))
