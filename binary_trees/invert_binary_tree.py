"""
Write a function that takes a Binary Tree and inverts it.
"""


# O(n) Time & O(d) Space where n is number of nodes and d is depth of tree
def invert_binary_tree(tree):
    if tree is not None:
        invert_binary_tree(tree.left)
        invert_binary_tree(tree.right)
        tree.left, tree.right = tree.right, tree.left
