"""
Write a function that takes in a binary tree and returns its diameter.
Diameter is defined as length of its logest path.
"""


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) Time & O(n) Space
def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    leftTreeData = getTreeInfo(tree.left)
    rightTreeData = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeData.height + rightTreeData.height
    maxDiameterSoFar = max(leftTreeData.diameter, rightTreeData.diameter)
    currentDiameter = max(maxDiameterSoFar, longestPathThroughRoot)
    currentHeight = 1 + max(leftTreeData.height, rightTreeData.height)

    return TreeInfo(currentDiameter, currentHeight)


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height
