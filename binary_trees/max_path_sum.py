# return max path sum
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def MPS(tree):
    _, maxPath = maxPathSum(tree)
    return maxPath


def maxPathSum(tree):
    if tree is not None:
        LSB, LS = maxPathSum(tree.left) if tree.left != None else (
            float('-inf'), float('-inf'))
        RSB, RS = maxPathSum(tree.right) if tree.right != None else (
            float('-inf'), float('-inf'))
        MCSB = max(LSB, RSB)
        MSB = max(MCSB+tree.value, tree.value)
        MST = max(MSB, LSB + tree.value + RSB)
        RMPS = max(LS, RS, MST)
        return (MSB, RMPS)


tree = BinaryTree(1)
tree.right = BinaryTree(3)
tree.right.right = BinaryTree(7)
tree.right.left = BinaryTree(6)
tree.left = BinaryTree(2)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)

print(MPS(tree))  # 18 // 5 + 2 + 1 + 3 + 7
