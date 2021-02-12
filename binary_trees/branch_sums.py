"""
Write a function that takes in a binary tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.
Additionally write a function that calculates the total sum.
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


def branchSums(root):
    currentSum = []
    calculateBranch(root, 0, currentSum)
    return currentSum


def totalSum(root):
    sum = 0
    sum = totalSumHelper(root, sum)
    return sum


def totalSumHelper(node, sum):
    if node is None:
        return
    if node.left is None and node.right is None:
        sum += node.value
        return sum
    else:
        sum = totalSumHelper(node.left, sum)
        sum = totalSumHelper(node.right, sum)
    return sum


def calculateBranch(node, runningSum, currentSum):
    if node is None:
        return
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        currentSum.append(newRunningSum)
        return
    calculateBranch(node.left, newRunningSum, currentSum)
    calculateBranch(node.right, newRunningSum, currentSum)


binary_tree = BinaryTree(1)
array = [2, 3, 4, 5]
binary_tree.insert(array)
print(totalSum(binary_tree))
# print(binary_tree.left.value)
# print(branchSums(binary_tree))
